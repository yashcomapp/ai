# scripts/build_part1_osc_otf.py
import json
import re

with open('backups/staging/mh9_scit_9_raw.json', 'r', encoding='utf-8') as f:
    raw_all = json.load(f)

raw_p1 = raw_all[0:89]

with open('scripts/ch9_p1_starter.json', 'r', encoding='utf-8') as f:
    part1_enhanced = json.load(f) # contains first 29 questions (Q1 to Q29)

print(f"Loaded {len(part1_enhanced)} starter questions (Q1 to Q29)")

# Generate OSC Q30 to Q73 (44 questions)
# Let's inspect each raw OSC question and construct rich 3-part pedagogical solution
osc_sols = {}

# We will define a comprehensive mapping for all 44 OSC questions
osc_map = {
    30: ("Soil mineral content",
         "Meteorological Elements vs Pedological Properties",
         "The state of the atmosphere is characterized by primary meteorological elements: air temperature, barometric pressure, relative humidity, wind speed and direction, cloud cover, and precipitation.",
         "Soil mineral content (such as nitrogen, phosphorus, and potassium levels) is a pedological/edaphic property of the lithosphere, not a primary meteorological element of the atmospheric fluid.",
         "Soil mineral content is a geological/edaphic property rather than an atmospheric meteorological element."),

    31: ("Providing weather forecasts and seismological observations",
         "Institutional Mandate of the India Meteorological Department",
         "The India Meteorological Department (IMD) is the principal government agency responsible for meteorological observations, weather forecasting, seismology, and detection of earthquakes across India.",
         "The IMD monitors national meteorological parameters and operates a national seismological network to track tectonic earthquakes, issuing warnings for cyclones, droughts, and tsunamis.",
         "Providing weather forecasts and seismological observations is the official primary statutory mandate of the IMD."),

    32: ("1875",
         "Historical Establishment of the IMD",
         "Following devastating tropical cyclones and the 1876 famine in India, the Government of India consolidated regional provincial meteorological observatories under a single unified national body.",
         "The India Meteorological Department was officially founded in **1875**, with Henry Francis Blanford appointed as the first Imperial Meteorological Reporter.",
         "1875 is the precise historical year in which the India Meteorological Department was established."),

    33: ("New Delhi",
         "Central Headquarters of the IMD",
         "The operational leadership of the IMD resides at its national headquarters, directing regional meteorological centres (RMCs) located across India.",
         "Originally established in Calcutta in 1875, the headquarters shifted to Shimla in 1905, to Pune in 1928, and finally to **New Delhi** (Mausam Bhavan, Lodhi Road) in 1944 where it directs national operations today.",
         "New Delhi is the official central headquarters directing the operations of the India Meteorological Department."),

    34: ("Planning crop sowing, irrigation, and harvesting schedules based on rain forecasts",
         "Agro-Meteorological Application in Agriculture",
         "Crop growth phenology (germination, flowering, grain filling) is critically vulnerable to moisture stress, thermal extremes, and untimely rainfall.",
         "Studying meteorology enables farmers to schedule crop sowing with monsoon onset, schedule canal irrigation efficiently, apply fertilizers before rains, and plan harvesting to prevent crop rot.",
         "Planning crop sowing, irrigation, and harvesting schedules based on rain forecasts is the fundamental agricultural application of meteorology."),

    35: ("Climate",
         "Distinction Between Weather and Climate",
         "Atmospheric conditions fluctuate over multiple temporal scales, necessitating formal distinction between short-term states and long-term statistical norms.",
         "While **weather** represents the day-to-day, short-term state of atmospheric elements, **climate** represents the statistical aggregate, average, and variability of weather conditions observed over an extended period (standardized by the WMO as a 30-year period).",
         "Climate is the formal scientific term denoting the average weather conditions recorded over an extended 30-year period."),

    36: ("Supercomputers running numerical weather prediction (NWP) models",
         "Computational Fluid Dynamics in Weather Prediction",
         "The atmosphere is a continuous fluid thermodynamic continuum governed by non-linear partial differential equations.",
         "Modern meteorological agencies utilize high-performance **supercomputers** (such as IMD's Pratyush and Mihir) to run Numerical Weather Prediction (NWP) models that simulate atmospheric equations across millions of 3D spatial grid cells.",
         "Supercomputers running numerical weather prediction (NWP) models are the primary computational tools used for modern forecasting."),

    37: ("Detecting precipitation location, intensity, and storm movement in real time",
         "Radar Remote Sensing in Meteorological Tracking",
         "Doppler Weather Radars emit directional pulses of microwave electromagnetic radiation that backscatter upon striking hydrometeors (raindrops, hail, snowflakes).",
         "By analyzing the returned echo amplitude (reflectivity) and Doppler phase shift, radar systems detect the precise geographic coordinates, rainfall intensity, vertical storm height, and internal wind velocities of severe storm cells in real time.",
         "Detecting precipitation location, intensity, and storm movement in real time is the primary operational role of weather radars."),

    38: ("Abnormal warming of surface waters in the central and eastern tropical Pacific Ocean",
         "El Niño Oceanic Phenomenon",
         "The El Niño-Southern Oscillation (ENSO) is a major coupled ocean-atmosphere climate cycle centered across the equatorial Pacific basin.",
         "**El Niño** (the warm phase) is defined by an abnormal, widespread rise in sea surface temperatures (SSTs) across the central and eastern tropical Pacific Ocean, weakening the equatorial trade winds and disrupting global atmospheric circulation.",
         "Abnormal warming of surface waters in the central and eastern tropical Pacific Ocean is the precise oceanographic definition of El Niño."),

    39: ("By capturing continuous visible and infrared imagery of cloud formations and cyclone tracks",
         "Satellite Meteorological Surveillance",
         "Geostationary and polar-orbiting meteorological satellites (such as INSAT-3D, INSAT-3DR, and Megha-Tropiques) provide continuous synoptic coverage of the Earth.",
         "Satellites carry advanced multispectral imagers capturing visible, infrared, and water vapor channels, allowing meteorologists to track cloud patch development, measure cloud-top temperatures, and monitor the spiral arms and eye of tropical cyclones over open oceans.",
         "Capturing continuous visible and infrared imagery of cloud formations and cyclone tracks is the primary role of weather satellites."),

    40: ("Barometer",
         "Barometric Atmospheric Pressure Measurement",
         "Atmospheric pressure is the force exerted per unit area by the weight of atmospheric gases above that point.",
         "A **barometer** (mercury barometer invented by Evangelista Torricelli, or digital aneroid barometer) measures atmospheric pressure in units of hectopascals (\\(\\text{hPa}\\)) or millimeters of mercury (\\(\\text{mmHg}\\)).",
         "Barometer is the specific scientific instrument utilized by meteorologists to measure atmospheric barometric pressure."),

    41: ("To measure upper-air temperature, humidity, pressure, and wind speed",
         "Upper-Air Atmospheric Profiling via Radiosondes",
         "Surface measurements alone cannot characterize the three-dimensional vertical structure of the troposphere and stratosphere.",
         "A **radiosonde** is a battery-powered instrument package suspended beneath a hydrogen or helium weather balloon that ascends through the atmosphere, measuring and transmitting vertical profiles of pressure, temperature, relative humidity, and GPS-derived wind vectors back to ground stations.",
         "Measuring upper-air temperature, humidity, pressure, and wind speed is the precise operational objective of radiosonde balloon soundings."),

    42: ("Urban Heat Island effect",
         "Urban Climatology & Microclimatic Warming",
         "Dense urban development fundamentally alters surface albedo, thermal mass, and vegetative cover compared to natural rural landscapes.",
         "The **Urban Heat Island (UHI)** effect describes the phenomenon where metropolitan urban areas experience significantly higher ambient air temperatures than surrounding rural hinterlands due to asphalt/concrete heat absorption, high building density, reduced evapotranspiration, and anthropogenic waste heat emissions.",
         "Urban Heat Island effect is the standard scientific term describing the elevated thermal profile of urban environments."),

    43: ("A line connecting points of equal atmospheric pressure",
         "Isobaric Contouring on Synoptic Weather Maps",
         "Spatial variations in atmospheric pressure drive horizontal wind motion and dictate large-scale weather systems.",
         "An **isobar** is an isoline drawn on a meteorological weather map connecting geographic points that share identical atmospheric pressure reduced to mean sea level, revealing high-pressure anticyclones, low-pressure cyclones, and pressure gradients.",
         "A line connecting points of equal atmospheric pressure is the exact definition of an isobar."),

    44: ("They help plan pesticide spraying, harvesting, and irrigation schedules without rain damage",
         "Agricultural Utility of Medium-Range Forecasts",
         "Medium-range weather forecasts span a time horizon of 3 to 10 days, bridging short-term tactical decisions and seasonal planning.",
         "A 3- to 10-day forecast gives farmers sufficient advance warning to schedule agricultural chemical spraying (which requires dry conditions so rain does not wash chemicals away), irrigate fields before dry spells, and harvest ripe grains before storm damage occurs.",
         "Planning pesticide spraying, harvesting, and irrigation schedules without rain damage represents the primary agricultural value of medium-range forecasts."),

    45: ("Measuring wind speed",
         "Anemometric Measurement of Air Velocity",
         "Wind represents the horizontal bulk motion of air parcels driven by atmospheric pressure gradients.",
         "An **anemometer** (such as a three-cup rotating anemometer or ultrasonic acoustic anemometer) measures wind speed by translating the rotational frequency of cups or sound transit times into velocity units (\\(\\text{m/s}\\) or \\(\\text{km/h}\\)).",
         "Measuring wind speed is the dedicated operational function of an anemometer."),

    46: ("Isotherms",
         "Thermal Contour Mapping in Meteorology",
         "Cartographic visualization of horizontal thermal gradients across geographic regions relies on standardized contour isolines.",
         "**Isotherms** are isolines drawn on meteorological charts connecting geographic locations exhibiting the same ambient air temperature at a given observational time.",
         "Isotherms is the precise scientific term for isolines connecting points of equal temperature."),

    47: ("By providing real-time data on wind shear, turbulence, fog, and thunderstorms along flight routes",
         "Aviation Meteorological Safety Advisories",
         "Aviation flight safety is fundamentally reliant on avoiding atmospheric hazards that impair aerodynamic lift or structural integrity.",
         "Aviation weather forecasts provide real-time aerodrome reports (METAR), terminal aerodrome forecasts (TAF), and sigmet warnings alerting pilots to severe convective storm cells, low-level wind shear, clear-air turbulence (CAT), and dense landing fog.",
         "Providing real-time data on wind shear, turbulence, fog, and thunderstorms along flight routes is how weather forecasting protects aviation safety."),

    48: ("Connecting areas receiving equal amounts of precipitation",
         "Isohyetal Precipitation Cartography",
         "Hydrological analysis of rainfall distribution over river basins and agricultural districts requires contoured precipitation mapping.",
         "An **isohyet** is an isoline plotted on a meteorological or climatological map connecting geographic stations that have recorded identical depths of rainfall or precipitation over a specified duration.",
         "Connecting areas receiving equal amounts of precipitation is the exact definition of an isohyet."),

    49: ("It describes temperature differences between the western and eastern Indian Ocean, impacting monsoon rainfall",
         "The Indian Ocean Dipole (IOD) Climate Mode",
         "The Indian Ocean Dipole (IOD) is a coupled ocean-atmosphere climate phenomenon characterized by anomalous sea surface temperature gradients across the equatorial Indian Ocean.",
         "A **Positive IOD** features warmer-than-normal sea surface temperatures in the western Indian Ocean (near the Arabian Sea) and cooler waters in the eastern Indian Ocean, driving enhanced atmospheric convection and boosting Indian monsoon rainfall.",
         "Describing temperature differences between the western and eastern Indian Ocean, impacting monsoon rainfall is the primary role of the Indian Ocean Dipole."),

    50: ("World Meteorological Organization (WMO)",
         "Global Meteorological Data Exchange & Governance",
         "Weather systems and atmospheric waves traverse national borders freely, requiring international coordination of observational standards.",
         "The **World Meteorological Organization (WMO)** is the specialized agency of the United Nations that standardizes meteorological instrumentation, coordinates the Global Observing System (GOS), and facilitates the worldwide real-time exchange of weather data through the Global Telecommunication System (GTS).",
         "World Meteorological Organization (WMO) is the international institutional body overseeing global weather data exchange."),

    51: ("Violent destructive winds, torrential rainfall, and coastal storm surges",
         "Tropical Cyclone Hazards & Coastal Impact",
         "Tropical cyclones derive immense energy from warm ocean waters (\\(> 26.5^\\circ\\text{C}\\)), manifesting as severe multi-hazard storm systems upon making landfall.",
         "The primary lethal hazards of a tropical cyclone are: (1) gale-force destructive winds exceeding \\(120\\text{--}200\\text{ km/h}\\), (2) torrential deluge causing flash floods, and (3) lethal **storm surges** that push ocean seawater inland across low-lying coastal belts.",
         "Violent destructive winds, torrential rainfall, and coastal storm surges constitute the primary triad of severe cyclone hazards."),

    52: ("Atmospheric humidity or moisture content",
         "Hygrometric Measurement of Atmospheric Moisture",
         "Water vapor in the atmosphere dictates cloud condensation, precipitation probability, and latent heat fluxes.",
         "A **hygrometer** (such as a psychrometer with wet-and-dry bulb thermometers, or a digital capacitive sensor) measures the humidity or moisture content (relative humidity, dew point) present in ambient air.",
         "Atmospheric humidity or moisture content is the specific meteorological parameter measured by a hygrometer."),

    53: ("To account for initial observational uncertainties by running multiple model simulations with slight variations",
         "Ensemble Forecasting & Non-Linear Chaos in NWP",
         "Due to the chaotic nature of atmospheric fluid dynamics, tiny initial observational measurement errors can lead to wildly diverging forecasts over time.",
         "In **ensemble forecasting**, supercomputers run an array (ensemble) of parallel model simulations with slightly perturbed, plausible initial conditions. The spread and clustering of these runs allow meteorologists to quantify forecast confidence and assign probabilities to extreme events.",
         "Accounting for initial observational uncertainties by running multiple model simulations with slight variations is the core scientific justification for ensemble forecasting."),

    54: ("The scientific study of the atmosphere, weather processes, and short-term atmospheric forecasting",
         "Scientific Definition & Scope of Meteorology",
         "The discipline of meteorology integrates thermodynamics, fluid dynamics, atmospheric chemistry, and remote sensing to understand the gaseous envelope of the Earth.",
         "**Meteorology** is defined as the scientific study of the physics, chemistry, and dynamics of the Earth's atmosphere, focusing on weather processes and short-term atmospheric forecasting.",
         "The scientific study of the atmosphere, weather processes, and short-term atmospheric forecasting is the foundational definition of meteorology."),

    55: ("Statistical forecasting model",
         "Statistical vs Dynamical Monsoon Modeling",
         "Monsoon forecasting methodologies are broadly bifurcated into statistical (empirical) models and dynamical (numerical) models.",
         "A **statistical forecasting model** relies on historical correlation and multi-variate regression equations relating past regional meteorological parameters (such as Eurasian snow cover or Pacific SSTs) to observed Indian monsoon rainfall totals.",
         "Statistical forecasting model is the specific type of model utilizing historical empirical relationships to predict rainfall."),

    56: ("High humidity reduces sweat evaporation, making it feel much hotter and more uncomfortable",
         "Relative Humidity & Human Evaporative Cooling",
         "The human body sheds excess heat primarily through the evaporation of perspiration from skin, a process that absorbs latent heat of vaporization (\\(\\sim 2.4\\text{ MJ/kg}\\)).",
         "When relative humidity is very high, the ambient air is already near moisture saturation, drastically slowing down the rate of sweat evaporation. As a result, sweat drips without cooling the body, trapping metabolic heat and making the apparent temperature feel much hotter and oppressive.",
         "High humidity reduces sweat evaporation, making it feel much hotter and more uncomfortable describes the physiological effect of humidity on thermal perception."),

    57: ("Solving hydro-thermodynamic equations of the atmosphere using supercomputers to forecast future weather states",
         "Mechanistic Nature of Numerical Weather Prediction",
         "Unlike empirical pattern-matching methods, Numerical Weather Prediction treats the atmosphere as a deterministic physical fluid continuum.",
         "NWP models use supercomputers to numerically integrate the foundational primitive equations of atmospheric physics (Navier-Stokes fluid equations, continuity of mass, thermodynamics, and moisture conservation) across a 3D computational grid to project future atmospheric states forward in time.",
         "Solving hydro-thermodynamic equations of the atmosphere using supercomputers to forecast future weather states is the primary function of NWP models."),

    58: ("El Niño-Southern Oscillation (ENSO)",
         "The Coupled ENSO Climate Oscillation",
         "The tropical Pacific Ocean undergoes a recurring, quasi-periodic coupled ocean-atmosphere oscillation that drives global climate teleconnections.",
         "**ENSO (El Niño-Southern Oscillation)** encompasses alternating warm phases (**El Niño**) and cool phases (**La Niña**) of equatorial Pacific sea surface temperatures, coupled with atmospheric pressure reversals between Darwin (Australia) and Tahiti (the Southern Oscillation), exerting major control over the Indian monsoon.",
         "El Niño-Southern Oscillation (ENSO) is the definitive ocean-atmosphere phenomenon governing equatorial Pacific thermal and pressure reversals."),

    59: ("To improve dynamic prediction models for forecasting Indian summer monsoon rainfall and extremes",
         "National Monsoon Mission Objectives",
         "The Ministry of Earth Sciences (MoES), Government of India, launched the National Monsoon Mission to transition India's operational monsoon forecasting from empirical statistical methods to state-of-the-art dynamical models.",
         "The primary objective of the **Monsoon Mission** was establishing a coupled ocean-atmosphere dynamical numerical modeling framework (high-resolution CFS and GFS models at IITM and NCMRWF) to significantly enhance the accuracy of seasonal, extended-range, and short-range monsoon forecasts.",
         "Improving dynamic prediction models for forecasting Indian summer monsoon rainfall and extremes is the core mandate of the National Monsoon Mission."),

    60: ("Differential heating and cooling rates between land and water masses",
         "Thermodynamic Driving Force of Mesoscale Sea and Land Breezes",
         "Adjacent land and water surfaces absorb and release incoming solar radiation at markedly different rates due to their contrasting specific heat capacities and physical properties.",
         "During the day, solar insolation heats low-heat-capacity land surfaces much faster than ocean water, creating a thermal low over land that pulls in cool, dense maritime air (**sea breeze**). At night, the land cools much faster through radiative heat loss while the sea stays warm, reversing the thermal gradient and causing air to blow from land to sea (**land breeze**).",
         "Differential heating and cooling rates between land and water masses is the physical mechanism driving diurnal land and sea breezes."),

    61: ("Measurement of the velocity and direction of precipitation particles (wind motion inside storms)",
         "The Doppler Effect in Radar Meteorology",
         "Standard conventional meteorological radars measure only the power reflectivity (amplitude) of backscattered microwave energy, revealing precipitation intensity.",
         "**Doppler weather radar** utilizes the Doppler frequency shift of backscattered microwave pulses to determine whether precipitation particles are moving toward or away from the radar antenna, providing real-time radial velocity and internal wind shear measurements inside developing storm cells and cyclones.",
         "Measurement of the velocity and direction of precipitation particles (wind motion inside storms) is the unique diagnostic advantage of Doppler radar."),

    62: ("Providing very short-term, high-resolution forecasts for immediate severe weather events spanning a few hours",
         "Meteorological Nowcasting Definition & Operational Role",
         "Severe mesoscale weather events like cloudbursts, severe thunderstorms, and squall lines evolve and dissipate over rapid timescales of minutes to hours.",
         "**Nowcasting** is defined by meteorological agencies (including IMD) as very short-range forecasting covering a lead time of 0 to 6 hours, utilizing high-resolution Doppler radar, satellite imagery, and automated weather stations to issue immediate warnings for imminent severe weather.",
         "Providing very short-term, high-resolution forecasts for immediate severe weather events spanning a few hours is the precise definition of nowcasting."),

    63: ("It deflects moving air and wind streams to the right in the Northern Hemisphere and to the left in the Southern Hemisphere",
         "Coriolis Force & Planetary Atmospheric Dynamics",
         "Because the Earth rotates eastward on its polar axis, any object or air parcel moving horizontally across the surface experiences an apparent inertial deflection known as the **Coriolis force**.",
         "The Coriolis acceleration (\\(2\\vec{\\Omega} \\times \\vec{v}\\)) deflects moving air streams to the **right** in the Northern Hemisphere and to the **left** in the Southern Hemisphere, playing an indispensable role in generating circular cyclonic vortices and governing global trade wind belts.",
         "Deflecting moving air and wind streams to the right in the Northern Hemisphere and to the left in the Southern Hemisphere correctly describes the Coriolis effect."),

    64: ("Its northward shift during summer draws moisture-laden south-westerly winds across the equator into the Indian subcontinent",
         "Seasonal Migration of the Intertropical Convergence Zone (ITCZ)",
         "The Intertropical Convergence Zone (ITCZ) is the global equatorial trough where the trade winds of the Northern and Southern Hemispheres converge.",
         "During the Northern Hemisphere summer, intense solar heating over the Indian landmass causes the ITCZ to shift far northward over the Indo-Gangetic plain. This migration pulls Southern Hemisphere south-east trade winds across the equator, where Coriolis deflection curves them into moisture-laden **South-West monsoon winds** across India.",
         "Its northward shift during summer draws moisture-laden south-westerly winds across the equator into the Indian subcontinent describes the primary significance of the ITCZ."),

    65: ("Transmitting vertical atmospheric profiles of temperature, pressure, and humidity via radio signals as they ascend",
         "In-Situ Atmospheric Telemetry via Radiosondes",
         "Characterizing upper-air atmospheric stability requires in-situ thermodynamic measurements at successive pressure levels up into the stratosphere.",
         "A **radiosonde** package contains sensors for pressure, temperature, and humidity, along with a radio transmitter. As the balloon ascends through the troposphere to altitudes of \\(20\\text{--}30\\text{ km}\\), it continuously beams real-time telemetry back to ground receiver stations to construct upper-air sounding diagrams (skew-T / tephigrams).",
         "Transmitting vertical atmospheric profiles of temperature, pressure, and humidity via radio signals as they ascend is the primary function of a radiosonde."),

    66: ("To route ships around high waves, severe gales, and tropical storms, ensuring crew safety and cargo integrity",
         "Maritime Meteorological Routing & Vessel Safety",
         "Navigating transoceanic cargo freighters and container vessels through open ocean basins exposes ships to extreme marine weather hazards.",
         "Continuous marine weather forecasts allow ship captains and maritime routing services to adjust navigation courses around high storm swells, dangerous gales, and tropical cyclone tracks, preventing capsizing, container loss, structural hull damage, and maritime casualties.",
         "Routing ships around high waves, severe gales, and tropical storms, ensuring crew safety and cargo integrity is why maritime transport relies on marine weather advisories."),

    67: ("Monsoon",
         "Etymological & Physical Definition of Monsoon",
         "The term 'monsoon' is derived from the Arabic word *mausim*, meaning 'season', historically used by Arabian sailors to describe seasonal winds.",
         "In meteorology, **monsoon** denotes a large-scale seasonal reversal of prevailing wind directions accompanied by corresponding changes in precipitation, exemplified by the South-West summer monsoon bringing life-giving rains to South Asia.",
         "Monsoon is the standard scientific term describing the seasonal wind reversal that brings summer rains to the Indian subcontinent."),

    68: ("To collect continuous, real-time local meteorological data without manual intervention",
         "Automated Weather Station (AWS) Networks",
         "Conventional manual observatories require trained human observers to record instruments at fixed synoptic hours (e.g., 08:30 and 17:30 IST), leaving temporal gaps.",
         "**Automated Weather Stations (AWS)** employ digital electronic sensors, microcontrollers, solar power, and satellite or cellular telemetry to collect and transmit meteorological data (temperature, pressure, humidity, wind, rainfall) continuously 24/7 without requiring manual human intervention.",
         "Collecting continuous, real-time local meteorological data without manual intervention is the primary objective of automated weather stations."),

    69: ("By steering surface pressure systems, steering storms, and dictating upper-level divergence and convergence",
         "Jet Streams & Tropospheric Telecoupling",
         "Jet streams are narrow, fast-flowing meandering air currents located in the upper troposphere (typically \\(9\\text{--}12\\text{ km}\\) altitude).",
         "Upper-air jet streams steer surface cyclones and anticyclones, determine storm tracks across mid-latitudes, and induce upper-level divergence that triggers upward vertical motion and storm development at the Earth's surface.",
         "Steering surface pressure systems, steering storms, and dictating upper-level divergence and convergence describes the major influence of upper-air jet streams on surface weather."),

    70: ("Tracking cyclonic storms in the Bay of Bengal and Arabian Sea and issuing timely landfall alerts",
         "Operational Role of Area Cyclone Warning Centers (ACWCs)",
         "India's peninsular geography with a \\(7500\\text{ km}\\) coastline borders two active tropical cyclonic ocean basins: the Bay of Bengal and the Arabian Sea.",
         "The IMD's dedicated Cyclone Warning Centers (such as ACWCs in Kolkata, Chennai, and Mumbai, and CWCs in Bhubaneswar, Visakhapatnam, and Ahmedabad) track cyclonic disturbances, generate cone-of-uncertainty landfall projections, and issue graded cyclone warning bulletins (yellow, orange, red alerts).",
         "Tracking cyclonic storms in the Bay of Bengal and Arabian Sea and issuing timely landfall alerts is the dedicated operational mission of IMD cyclone warning centers."),

    71: ("Depth of accumulated precipitation in millimeters over a specific period",
         "Rain Gauge Precipitation Measurement",
         "Liquid precipitation that reaches the ground must be measured quantitatively to assess hydrological influx and agricultural moisture.",
         "A **rain gauge** (standard Symons gauge or automatic tipping-bucket gauge) collects rainfall falling over a standardized aperture area and measures the total accumulated depth of water in **millimeters (\\(\\text{mm}\\))** that would cover a flat horizontal surface without evaporation or runoff.",
         "Depth of accumulated precipitation in millimeters over a specific period is the exact measurement provided by a rain gauge."),

    72: ("They combine outputs from various independent forecasting models to reduce individual model bias and improve overall forecast skill",
         "Multi-Model Ensemble (MME) Prediction Superiority",
         "Every individual numerical weather prediction model incorporates unique mathematical approximations, spatial grid resolutions, and physical parameterizations that introduce systematic biases.",
         "**Multi-Model Ensemble (MME)** forecasting synthesizes outputs from diverse, state-of-the-art independent models (e.g., IMD-GFS, ECMWF, NCEP, UKMO). By averaging across independent model formulations, individual systematic errors cancel out, resulting in a composite forecast that consistently outperforms any single deterministic model.",
         "Combining outputs from various independent forecasting models to reduce individual model bias and improve overall forecast skill is why multi-model ensembles are superior."),

    73: ("Enhancing moisture transport toward the Indian subcontinent, supporting favorable monsoon rains",
         "Positive Indian Ocean Dipole Impact on Monsoon",
         "The phase and amplitude of the Indian Ocean Dipole directly modulate the regional moisture conveyor belt feeding the Indian subcontinent.",
         "In a **Positive IOD** phase, sea surface temperatures are unusually warm in the western Indian Ocean near the Arabian Sea and cooler in the eastern Indian Ocean near Sumatra. This thermal setup enhances convective activity and evaporation over the Arabian Sea, pumping abundant moisture into the South-West monsoon winds and supporting favorable, above-average monsoon rains across India.",
         "Enhancing moisture transport toward the Indian subcontinent, supporting favorable monsoon rains describes the impact of a positive IOD phase.")
}

# Add OSC Q30 to Q73
for idx in range(29, 73):
    raw_q = raw_p1[idx]
    q_num = idx + 1
    raw_ans = raw_q['correctAnswer']
    opts = raw_q['options']
    
    # Identify correct letter
    found_letter = None
    letters = ['A', 'B', 'C', 'D']
    for opt_idx, opt in enumerate(opts):
        if raw_ans.strip().lower() in opt.strip().lower() or opt.strip().lower() in raw_ans.strip().lower():
            found_letter = letters[opt_idx]
            break
    if not found_letter:
        print(f"Warning: match not found for Q{q_num}, raw_ans: {raw_ans}")
        found_letter = "A"
        
    ans_text, header_topic, p1_principle, p2_process, p3_correct_exp = osc_map[q_num]
    
    # Construct 3-part solution with aligned options
    sol_lines = [
        f"### 1. Scientific Principle & {header_topic}:",
        p1_principle,
        "",
        "### 2. Physical Process & Atmospheric / Computational Dynamics:",
        p2_process,
        "",
        "### 3. Step-by-Step Option & Misconception Analysis:"
    ]
    
    for opt_idx, letter in enumerate(letters):
        opt_text = opts[opt_idx]
        if letter == found_letter:
            sol_lines.append(f"- **Option {letter} is correct.** {p3_correct_exp}")
        else:
            sol_lines.append(f"- **Option {letter} is incorrect.** '{opt_text}' does not accurately represent the primary scientific principle in this meteorological context.")
            
    solution_text = "\n".join(sol_lines)
    
    item = {
        "questionCode": raw_q['questionCode'],
        "type": "OSC",
        "text": raw_q['text'],
        "options": opts,
        "correctAnswer": found_letter,
        "solution": solution_text
    }
    part1_enhanced.append(item)

print(f"Added OSC questions, total now: {len(part1_enhanced)}")

# OTF Q74 to Q89 (16 questions)
otf_data = {
    74: ("True", """### 1. Scientific Principle & Solar Insolation as the Ultimate Atmospheric Driver:
The Sun is the primary external source of energy powering Earth's climate system.

### 2. Physical Process & Differential Solar Radiation:
- Incoming solar radiation (insolation) is absorbed unevenly by the spherical Earth due to axial tilt, latitude, and contrasting albedos between oceans, ice sheets, and land surfaces.
- This latitudinal differential heating generates global thermal and pressure gradients, which in turn drive planetary wind systems, ocean currents, the hydrological cycle, and all meteorological elements.

### 3. Step-by-Step Option & Misconception Analysis:
- **Statement Evaluation:** The statement asserts that changes in meteorological elements are driven primarily by energy received from the Sun. This is scientifically **True**.
- Solar insolation is the foundational thermodynamic energy source fueling all atmospheric weather dynamics."""),

    75: ("True", """### 1. Scientific Principle & Multi-Platform Meteorological Observation:
Comprehensive atmospheric surveillance requires observing both surface boundary layers and the deep tropospheric column.

### 2. Physical Process & Data Synergy:
- Modern weather forecasting relies on fusing data from **surface systems** (automated weather stations, coastal radars, ocean buoys, ships) with **space-based systems** (geostationary and polar satellites measuring multispectral radiance, atmospheric soundings, and cloud drift winds).
- Neither surface nor space-based platforms alone are sufficient; both are indispensable for global numerical data assimilation.

### 3. Step-by-Step Option & Misconception Analysis:
- **Statement Evaluation:** The statement states that weather forecasting requires continuous collection of data using both surface and space-based observation systems. This is **True**.
- Integrating surface observatories and satellite constellations is mandatory for accurate weather prediction."""),

    76: ("True", """### 1. Scientific Principle & Weather vs Climate Temporal Scales:
Atmospheric phenomena occur across vast temporal hierarchies spanning hours to geological epochs.

### 2. Physical Process & Dynamic Variation vs Statistical Norms:
- **Weather** describes the instantaneous, short-term physical state of the atmosphere (e.g., temperature, rain, wind) that can change drastically within minutes or hours due to passing convective cells or front passages.
- In contrast, **climate** represents the statistical aggregate, mean, and frequency distribution of weather patterns over multiple decades (standardized as a 30-year climatological baseline), shifting slowly over decadal, centennial, or millennial timescales.

### 3. Step-by-Step Option & Misconception Analysis:
- **Statement Evaluation:** The statement asserts that weather can change drastically within a few hours, whereas climate changes slowly over decades or centuries. This is **True**.
- Weather represents rapid short-term states, while climate reflects multi-decadal statistical norms."""),

    77: ("True", """### 1. Scientific Principle & La Niña Oceanic Dynamics:
La Niña represents the cool oceanic phase of the El Niño-Southern Oscillation (ENSO) cycle across the equatorial Pacific basin.

### 2. Physical Process & Equatorial Upwelling & Trade Winds:
- During La Niña, unusually strong easterly trade winds drive intense equatorial upwelling of cold, nutrient-rich deep ocean water along the coasts of Peru and Ecuador.
- As a consequence, sea surface temperatures across the central and eastern tropical Pacific drop significantly below their long-term climatological averages, altering global Walker and Hadley circulation cells.

### 3. Step-by-Step Option & Misconception Analysis:
- **Statement Evaluation:** The statement asserts that La Niña conditions are associated with cooler-than-normal sea surface temperatures in the central and eastern Pacific. This is **True**.
- Cooler-than-average equatorial Pacific sea surface temperatures are the definitive physical hallmark of La Niña."""),

    78: ("False", """### 1. Scientific Principle & Data Assimilation & Observational Integration:
Numerical meteorological models require comprehensive data assimilation across all vertical levels of the atmosphere.

### 2. Physical Process & Ground Station Indispensability:
- Local and regional weather forecasting models cannot rely exclusively on satellite observations.
- Satellites provide indirect radiometric soundings, but direct, physical surface measurements from ground-based Automated Weather Stations (AWS)—including accurate surface pressure, 2-meter air temperature, and rain gauge records—are critical for anchoring model boundary layers and verifying satellite retrievals.

### 3. Step-by-Step Option & Misconception Analysis:
- **Statement Evaluation:** The statement claims that local weather forecasting models rely exclusively on satellite data and ignore all ground station observations. This is **False**.
- Ground-based surface observations are essential anchors for data assimilation in weather forecasting models."""),

    79: ("True", """### 1. Scientific Principle & Short-Range Forecast Temporal Hierarchy:
Meteorological forecasts are organized into operational temporal lead times defined by the World Meteorological Organization.

### 2. Physical Process & Operational Application of Short-Range Forecasts:
- **Short-range forecasts** encompass the time window from 0 to 48 hours.
- Because deterministic skill is highest over this short temporal range, short-range forecasts provide vital operational guidance for daily aviation scheduling, municipal flood gates, disaster alerts, and citizen activities.

### 3. Step-by-Step Option & Misconception Analysis:
- **Statement Evaluation:** The statement asserts that short-range weather forecasts cover periods of less than 48 hours and provide high operational value for daily planning. This is **True**.
- Forecasts spanning up to 48 hours are classified as short-range and hold high operational utility."""),

    80: ("False", """### 1. Scientific Principle & Defining Climate Change:
Climate change is defined scientifically by long-term, statistically significant shifts in the mean state of the climate or its variability.

### 2. Physical Process & Multi-Decadal Baselines:
- A brief atmospheric anomaly lasting a few days or a single week (such as an isolated heatwave or a cold snap) is categorized as a transient **weather anomaly**, not climate change.
- Under WMO conventions, **climate change** refers to persistent trends or structural shifts in atmospheric and oceanic variables that endure for decades or longer (typically multi-decadal to centennial spans).

### 3. Step-by-Step Option & Misconception Analysis:
- **Statement Evaluation:** The statement asserts that climate change refers exclusively to short-term weather anomalies lasting less than a single week. This is **False**.
- Short-term weekly fluctuations are transient weather anomalies; climate change spans multi-decadal timescales."""),

    81: ("False", """### 1. Scientific Principle & Theoretical Basis of Meteorology:
Meteorology is a rigorous physical science rooted in the mathematical laws of thermodynamics and classical fluid dynamics.

### 2. Physical Process & Numerical Modeling:
- Weather forecasting does not rely merely on qualitative empirical observation; it involves solving the primitive hydro-thermodynamic partial differential equations of atmospheric fluid motion.
- Modern forecasts are produced by ingesting billions of observational data points into supercomputers running complex mathematical Numerical Weather Prediction (NWP) models.

### 3. Step-by-Step Option & Misconception Analysis:
- **Statement Evaluation:** The statement claims that weather forecasts are purely observational and do not involve any mathematical or physical modeling. This is **False**.
- Modern forecasting is fundamentally built upon complex mathematical and physical fluid dynamic models."""),

    82: ("True", """### 1. Scientific Principle & Applied Marine Meteorology & Public Safety:
Marine weather prediction provides specialized risk mitigation for artisanal and commercial deep-sea fishing communities.

### 2. Physical Process & Marine Bulletins & Coastal Warnings:
- The IMD issues specialized daily marine weather bulletins, coastal sea state forecasts, and squall warnings broadcast via coastal radio, mobile apps (such as SAGAR VANI), and harbor signals.
- These advisories detail expected wave heights, gale wind speeds, and approaching depressions, advising fishermen when sea conditions are dangerous and prohibiting them from venturing into deep waters.

### 3. Step-by-Step Option & Misconception Analysis:
- **Statement Evaluation:** The statement asserts that the IMD provides specialized forecasts specifically tailored for fishermen venturing into coastal and deep-sea waters. This is **True**.
- Dedicated marine bulletins and sea state warnings for fishermen are an essential statutory public service of the IMD."""),

    83: ("False", """### 1. Scientific Principle & Climatological Time Windows:
Determining the climate of a geographical territory requires eliminating short-term stochastic weather noise through long-term statistical averaging.

### 2. Physical Process & 30-Year Normals:
- A few days of atmospheric observation capture only fleeting weather conditions (e.g., a passing rainy day or a transient cold front).
- The World Meteorological Organization defines the **climate** of a region as the statistical distribution, average, and extremes of atmospheric elements measured over a minimum period of **30 consecutive years** (climatological normal period).

### 3. Step-by-Step Option & Misconception Analysis:
- **Statement Evaluation:** The statement claims that climate is determined by observing atmospheric conditions over a short span of a few days. This is **False**.
- Climate determination requires long-term statistical observation over standard 30-year periods."""),

    84: ("True", """### 1. Scientific Principle & Institutional Governance of Meteorology in India:
National meteorological agencies operate under specific federal ministerial frameworks responsible for Earth system sciences.

### 2. Physical Process & Administrative Architecture:
- The **India Meteorological Department (IMD)** functions as an attached subordinate office under the **Ministry of Earth Sciences (MoES)**, Government of India.
- MoES coordinates the unified national mandates of the IMD, the National Centre for Medium Range Weather Forecasting (NCMRWF), the Indian Institute of Tropical Meteorology (IITM), and the Indian National Centre for Ocean Information Services (INCOIS).

### 3. Step-by-Step Option & Misconception Analysis:
- **Statement Evaluation:** The statement states that the India Meteorological Department operates under the Ministry of Earth Sciences, Government of India. This is **True**.
- The IMD is officially administered under the Ministry of Earth Sciences (MoES)."""),

    85: ("False", """### 1. Scientific Principle & The Predictability Horizon in Atmospheric Physics:
The atmosphere is a chaotic, non-linear dynamical system characterized by sensitive dependence on initial conditions.

### 2. Physical Process & Deterministic Limits:
- In 1963, Edward Lorenz established that deterministic numerical weather predictions lose detailed accuracy beyond roughly two weeks due to the exponential growth of initial measurement errors.
- Therefore, no computer model can ever predict local atmospheric conditions with 100% absolute deterministic certainty several months in advance; long-range seasonal forecasts can only be expressed probabilistically.

### 3. Step-by-Step Option & Misconception Analysis:
- **Statement Evaluation:** The statement claims that weather forecasting models can predict local atmospheric conditions with 100% absolute deterministic certainty several months in advance. This is **False**.
- Deterministic predictability is bounded by non-linear chaos; multi-month forecasts are inherently probabilistic."""),

    86: ("True", """### 1. Scientific Principle & Satellite Surveillance of Cyclogenesis:
Tropical cyclones develop over vast, warm ocean basins where in-situ surface observational stations are virtually non-existent.

### 2. Physical Process & Orbital Remote Sensing:
- Earth observation satellites in geostationary orbits (such as INSAT-3D and INSAT-3DR) capture continuous multispectral imagery of the Indian Ocean basin every 15 to 30 minutes.
- Meteorologists use visible and thermal infrared imagery to detect low-pressure cloud clusters, monitor vortex spiral bands, measure sea surface temperatures, and track the central eye of cyclones from formation to landfall.

### 3. Step-by-Step Option & Misconception Analysis:
- **Statement Evaluation:** The statement states that satellite imagery allows meteorologists to monitor the genesis and track of tropical cyclones over open oceans. This is **True**.
- Satellite remote sensing is the indispensable technology enabling early detection and tracking of oceanic cyclones."""),

    87: ("False", """### 1. Scientific Principle & Vertical Extent of Meteorology:
Meteorology is the science of the three-dimensional atmospheric fluid envelope, not merely a surface science.

### 2. Physical Process & Tropospheric-Stratospheric Dynamics:
- Surface weather events (rain, cold fronts, heatwaves) are steered by upper-air tropospheric jet streams, baroclinic waves, upper-level divergence, and stratospheric-tropospheric couplings.
- Meteorology investigates the atmosphere from the surface boundary layer up through the troposphere, stratosphere, and mesosphere using balloon radiosondes, radars, and satellites.

### 3. Step-by-Step Option & Misconception Analysis:
- **Statement Evaluation:** The statement claims that the study of meteorology is strictly confined to surface observations and ignores upper-air atmospheric layers. This is **False**.
- Meteorology investigates the entire three-dimensional vertical structure of the atmosphere."""),

    88: ("False", """### 1. Scientific Principle & ENSO Spatial Heterogeneity:
While El Niño is a global climate driver, its regional impacts across the globe and within individual subcontinents are spatially complex and heterogeneous.

### 2. Physical Process & El Niño Rainfall Suppression:
- Historically, an El Niño event in the equatorial Pacific is statistically associated with a **suppression** or weakening of the Indian summer monsoon (frequently causing rainfall deficits or agricultural droughts), rather than bringing above-average rainfall.
- Moreover, its impact varies geographically: some sub-regions may receive normal rain while others suffer severe drought, and anomalous conditions depend heavily on concurrent Indian Ocean Dipole (IOD) interactions.

### 3. Step-by-Step Option & Misconception Analysis:
- **Statement Evaluation:** The statement claims that El Niño events consistently bring above-average rainfall across all regions of the Indian subcontinent without exception. This is **False**.
- El Niño typically weakens Indian monsoon rains and increases drought risk rather than causing above-average rainfall."""),

    89: ("False", """### 1. Scientific Principle & Hydro-Meteorology & Urban Flood Management:
Urban flash flooding occurs when intense localized rainfall exceeds the drainage absorption capacity of paved municipal infrastructure.

### 2. Physical Process & Radar Nowcasting for Drainage Management:
- Modern urban flood risk management relies directly on meteorological radar nowcasting, high-resolution quantitative precipitation estimates (QPE), and automated rain gauges.
- Early meteorological alerts (e.g., IMD's urban flood warning systems in Mumbai and Chennai) enable city authorities to open storm drainage sluice gates, activate de-watering pumps, divert traffic from low-lying underpasses, and mobilize emergency rescue teams before waters peak.

### 3. Step-by-Step Option & Misconception Analysis:
- **Statement Evaluation:** The statement claims that the study of meteorology has no practical impact on managing urban flash floods or river inundation events. This is **False**.
- Real-time meteorological nowcasting and radar observations are vital for active urban flood warning and drainage control.""")
}

for idx in range(73, 89):
    raw_q = raw_p1[idx]
    q_num = idx + 1
    ans_val, sol = otf_data[q_num]
    
    item = {
        "questionCode": raw_q['questionCode'],
        "type": "OTF",
        "text": raw_q['text'],
        "options": ["True", "False"],
        "correctAnswer": ans_val,
        "solution": sol
    }
    part1_enhanced.append(item)

print(f"Added OTF questions, total now: {len(part1_enhanced)}")

# Write to scripts/ch9_part1.js
output_js = "// scripts/ch9_part1.js\n"
output_js += "// MH-9-SCIT-9-9.1.1 Meteorology, IMD, Weather Forecasting, Monsoon Prediction Models (89 questions, Q1 to Q89)\n"
output_js += "const ch9_part1 = " + json.dumps(part1_enhanced, indent=2, ensure_ascii=False) + ";\n\n"
output_js += "module.exports = { ch9_part1 };\n"

with open('scripts/ch9_part1.js', 'w', encoding='utf-8') as f:
    f.write(output_js)

print("Saved scripts/ch9_part1.js successfully!")
