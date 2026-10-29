# scripts/build_part1_full.py
import json
import re

with open('backups/staging/mh9_scit_9_raw.json', 'r', encoding='utf-8') as f:
    raw_all = json.load(f)

raw_p1 = raw_all[0:89] # Q1 to Q89

print(f"Loaded {len(raw_p1)} raw questions for Topic 9.1.1")

oar_options = [
    "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).",
    "Both Assertion (A) and Reason (R) are true, but Reason (R) is NOT the correct explanation of Assertion (A).",
    "Assertion (A) is true, but Reason (R) is false.",
    "Assertion (A) is false, but Reason (R) is true."
]

# We will generate rich pedagogical solutions for Q1 to Q89
part1_enhanced = []

# Q1 to Q15 (OAR)
oar_sols = {
    1: ("C", """### 1. Scientific Principle & Scope of Meteorology:
Meteorology is the atmospheric branch of Earth science that investigates the physical and chemical processes occurring within the troposphere and stratosphere, analyzing the continuous thermodynamic interactions between air, solar radiation, land masses, and oceanic reservoirs.

### 2. Physical Process & Atmospheric Seasonality:
- The fundamental premise of meteorology is predicting atmospheric changes governed by differential solar heating, fluid dynamics, and global circulation.
- Contrary to Reason (R), tropical weather patterns are never static; they are highly dynamic, experiencing intense seasonal shifts driven by the migration of the Intertropical Convergence Zone (ITCZ), tropical easterly jets, cyclonic disturbances, and seasonal monsoon reversals.
- Because weather is inherently variable across daily and seasonal timescales, Reason (R) is factually and scientifically incorrect.

### 3. Step-by-Step Option & Misconception Analysis:
- **Assertion (A) Evaluation:** True. Meteorology studies atmospheric interrelationships between air, water, and land to forecast weather phenomena.
- **Reason (R) Evaluation:** False. Tropical weather patterns are dynamic and undergo marked seasonal changes rather than remaining static.
- **Causal Connection:** Because Reason (R) is false while Assertion (A) is true, Option C is the correct classification.
- **Option C is correct.** Assertion (A) is true, but Reason (R) is false."""),

    2: ("A", """### 1. Scientific Principle & Tropical Cyclone Dynamics:
Tropical cyclones are intense cyclonic vortices characterized by low central pressure, gale-force rotating winds, and torrential rainfall, generating deadly coastal storm surges.

### 2. Physical Process & Early Warning Impact:
- Modern meteorological forecasting utilizes geostationary satellites (e.g., INSAT-3D/3DR) and coastal Doppler Weather Radars to detect cyclogenesis and project landfall trajectories up to \\(72\\text{--}120\\text{ hours}\\) in advance.
- These accurate track predictions enable disaster management authorities to trigger pre-emptive evacuation protocols, moving vulnerable coastal fishing communities and low-lying populations to fortified cyclone shelters prior to landfall.
- As demonstrated during recent Arabian Sea and Bay of Bengal cyclones, timely evacuation directly curtails human mortality to near zero.

### 3. Step-by-Step Option & Misconception Analysis:
- **Assertion (A) Evaluation:** True. Timely cyclone tracking and early forecasts dramatically reduce mortality and asset destruction.
- **Reason (R) Evaluation:** True. Advance warnings empower authorities to evacuate endangered coastal populations before storm surge landfall.
- **Causal Connection:** Reason (R) provides the direct operational mechanism that makes Assertion (A) true.
- **Option A is correct.** Both Assertion and Reason are true, and Reason is the correct explanation of Assertion."""),

    3: ("A", """### 1. Scientific Principle & Agronomic Agro-Climatology:
The Indian summer monsoon (South-West monsoon) is the primary hydrological driver of the subcontinent's agricultural cycle, supplying over \\(70\\%\\) of India's total annual precipitation between June and September.

### 2. Physical Process & Rainfed Agriculture:
- Across India, approximately \\(50\\%\\text{--}55\\%\\) of the net sown area lacks canal or deep-tube-well irrigation infrastructure and depends strictly on rainfed agriculture (Kharif season crops such as rice, pulses, cotton, and groundnuts).
- Sowing dates, seedling emergence, and vegetative canopy development are calibrated to the seasonal onset of monsoon winds and the spatial distribution of monsoon depressions.
- Variations or delays in monsoon precipitation immediately threaten crop survival and ground water recharge.

### 3. Step-by-Step Option & Misconception Analysis:
- **Assertion (A) Evaluation:** True. Indian agriculture is inextricably tied to the arrival, volume, and distribution of monsoon rainfall.
- **Reason (R) Evaluation:** True. A major proportion of cultivated agricultural land depends directly on rainfed farming without assured canal irrigation.
- **Causal Connection:** Reason (R) provides the foundational agronomic reason for Assertion (A).
- **Option A is correct.** Both Assertion and Reason are true, and Reason is the correct explanation of Assertion."""),

    4: ("A", """### 1. Scientific Principle & Barometric Pressure Dynamics:
Atmospheric pressure represents the weight of the air column above a given unit area on the Earth's surface (standard mean sea-level pressure is \\(1013.25\\text{ hPa}\\)).

### 2. Physical Process & Low-Pressure Formation:
- A steep, rapid drop in barometric pressure signals the development or approach of an intense atmospheric low-pressure system (such as a depression, squall line, or cyclonic vortex).
- Because fluids move down pressure gradients from high to low pressure, surrounding air rushes rapidly toward the low-pressure center.
- This convergence forces warm, moist air to ascend vigorously (updrafts); as the air rises, it expands adiabatically, cools to its dew point, and condenses into towering cumulonimbus clouds that produce heavy squalls, thunderstorms, and adverse weather.

### 3. Step-by-Step Option & Misconception Analysis:
- **Assertion (A) Evaluation:** True. A sharp drop in barometric pressure serves as a classical meteorological precursor to stormy weather.
- **Reason (R) Evaluation:** True. Rapidly falling pressure creates steep horizontal pressure gradients, driving air convergence, ascent, adiabatic cooling, and storm development.
- **Causal Connection:** Reason (R) provides the physical fluid dynamic explanation for Assertion (A).
- **Option A is correct.** Both Assertion and Reason are true, and Reason is the correct explanation of Assertion."""),

    5: ("A", """### 1. Scientific Principle & Orographic Precipitation:
Orographic precipitation occurs when topographically elevated relief barriers (such as mountain ranges like the Western Ghats or the Himalayas) intercept prevailing horizontal moisture-laden wind currents.

### 2. Physical Process & Adiabatic Lapse Rate:
- When moist south-westerly maritime air currents encounter an elevated mountain barrier, they are forced to ascend the windward slope.
- As the air mass rises, ambient atmospheric pressure decreases, causing the air to undergo **adiabatic expansion and cooling** at the dry adiabatic lapse rate (\\(\\sim 9.8^\\circ\\text{C/km}\\)).
- Upon reaching saturation (dew point), water vapor condenses into cloud droplets, releasing latent heat of condensation and generating heavy orographic precipitation on the windward slope.
- Once the air crests the ridge and descends the leeward side, it compresses, warms adiabatically, and dries out, creating a rain-shadow zone.

### 3. Step-by-Step Option & Misconception Analysis:
- **Assertion (A) Evaluation:** True. Windward mountain slopes receive intense, persistent orographic rainfall.
- **Reason (R) Evaluation:** True. Forced mechanical ascent triggers adiabatic expansion, cooling, condensation, and rainout.
- **Causal Connection:** Reason (R) states the exact thermodynamic mechanism causing the rainfall described in Assertion (A).
- **Option A is correct.** Both Assertion and Reason are true, and Reason is the correct explanation of Assertion."""),

    6: ("A", """### 1. Scientific Principle & Deterministic Chaos in Fluid Dynamics:
The Earth's atmosphere is a continuous, non-linear fluid thermodynamic system governed by the Navier-Stokes equations of fluid motion.

### 2. Physical Process & The Butterfly Effect:
- In 1963, meteorologist Edward Lorenz demonstrated that atmospheric circulation models exhibit sensitive dependence on initial conditions (**deterministic chaos**).
- Even infinitesimally small errors or rounding differences in initial temperature, pressure, or wind measurements grow exponentially over time during numerical integration:
  \\[\\epsilon(t) \\approx \\epsilon_0 e^{\\lambda t}\\]
- Consequently, while short-range deterministic forecasts (\\(1\\text{--}3\\text{ days}\\)) are highly accurate, skill drops rapidly beyond \\(10\\text{--}14\\text{ days}\\), turning forecasts into probabilistic approximations.

### 3. Step-by-Step Option & Misconception Analysis:
- **Assertion (A) Evaluation:** True. Forecasting skill degrades significantly and uncertainty rises sharply beyond a 10 to 14 day horizon.
- **Reason (R) Evaluation:** True. Atmospheric dynamics is a chaotic non-linear system where microscopic initial observational errors amplify exponentially.
- **Causal Connection:** Reason (R) describes the mathematical and physical basis of the predictability limit in Assertion (A).
- **Option A is correct.** Both Assertion and Reason are true, and Reason is the correct explanation of Assertion."""),

    7: ("A", """### 1. Scientific Principle & Specific Heat Capacity of Water:
Water has an exceptionally high specific heat capacity (\\(c = 4184\\text{ J/(kg}\\cdot\\text{K)}\\)), approximately four to five times greater than that of dry soil, granite, or rock (\\(c \\sim 800\\text{--}1000\\text{ J/(kg}\\cdot\\text{K)}\\)).

### 2. Physical Process & Maritime Temperature Moderation:
- Because of its high thermal inertia and deep mixing layers, ocean water heats up much more slowly during daytime and cools down much more slowly during nighttime compared to adjacent land surfaces.
- During the day, warm air over land rises, drawing in cool maritime air (**sea breeze**).
- At night, the land cools rapidly while the ocean remains warmer, reversing the airflow (**land breeze**).
- This continuous diurnal thermal buffering prevents extreme daily temperature fluctuations, imparting an equable maritime climate to coastal regions.

### 3. Step-by-Step Option & Misconception Analysis:
- **Assertion (A) Evaluation:** True. Coastal zones experience moderate diurnal temperature ranges compared to continental interiors.
- **Reason (R) Evaluation:** True. High specific heat capacity of oceans drives diurnal land and sea breezes that buffer thermal extremes.
- **Causal Connection:** Reason (R) correctly explains the thermodynamic cause of Assertion (A).
- **Option A is correct.** Both Assertion and Reason are true, and Reason is the correct explanation of Assertion."""),

    8: ("A", """### 1. Scientific Principle & Disaster Risk Reduction (DRR):
Disaster vulnerability is a function of hazard exposure, structural susceptibility, and coping capacity. Early warning systems constitute a cornerstone of non-structural disaster risk mitigation.

### 2. Physical Process & Pre-Emptive Mitigation:
- Multi-hazard early warning systems integrate meteorological observation networks, automated hydrological gauges, and numerical storm surge models.
- When extreme thresholds (such as cloudbursts, severe cyclones, or flash floods) are detected, automated alert dissemination triggers structured standard operating procedures (SOPs):
  - Pre-emptive shutdown of power grids and railway operations to prevent electrocution and derailments.
  - Deployment of National Disaster Response Force (NDRF) teams to high-risk zones.
  - Safe evacuation of livestock and vulnerable citizen populations to reinforced shelters.

### 3. Step-by-Step Option & Misconception Analysis:
- **Assertion (A) Evaluation:** True. Robust early warning systems substantially minimize disaster damage and community vulnerability.
- **Reason (R) Evaluation:** True. Timely alerts allow municipal agencies to activate preventative infrastructure measures and mobilize emergency shelters.
- **Causal Connection:** Reason (R) provides the concrete operational actions that make Assertion (A) effective.
- **Option A is correct.** Both Assertion and Reason are true, and Reason is the correct explanation of Assertion."""),

    9: ("A", """### 1. Scientific Principle & Hypsometric Law & Barometric Fall:
Atmospheric pressure decreases exponentially with increasing height above sea level according to the barometric formula:
\\[P(z) = P_0 \\exp\\left(-\\frac{M g z}{R T}\\right)\\]

### 2. Physical Process & High-Altitude Environmental Stress:
- At high mountain altitudes (e.g., above \\(4000\\text{--}6000\\text{ meters}\\)), ambient barometric pressure and the partial pressure of oxygen (\\(P_{\\text{O}_2}\\)) drop to less than half their sea-level values, predisposing climbers to acute mountain sickness (AMS) and pulmonary/cerebral edema.
- Concurrently, air density decreases and wind velocity increases, dramatically elevating wind-chill equivalent temperatures and causing rapid convective heat loss that accelerates life-threatening hypothermia and frostbite.

### 3. Step-by-Step Option & Misconception Analysis:
- **Assertion (A) Evaluation:** True. High-altitude mountaineering requires continuous, vigilant monitoring of barometric and thermal conditions.
- **Reason (R) Evaluation:** True. Exponential drops in atmospheric pressure and oxygen concentration combined with wind-chill induce severe physiological hazards.
- **Causal Connection:** Reason (R) explains the direct biophysical hazards justifying Assertion (A).
- **Option A is correct.** Both Assertion and Reason are true, and Reason is the correct explanation of Assertion."""),

    10: ("A", """### 1. Scientific Principle & Aviation Meteorology:
Aircraft performance, navigation, and passenger safety are directly governed by the physical properties of the ambient air through which the aircraft moves.

### 2. Physical Process & Severe Weather Hazards to Flight:
- Commercial aircraft cruise at high subsonic speeds where atmospheric disturbances pose critical risks:
  - **Cumulonimbus Clouds & Thunderstorms:** Generate violent convective updrafts, downdrafts, microbursts, and severe hail damage.
  - **Low-Level Wind Shear:** Causes sudden loss of airspeed and lift during takeoff and landing phases.
  - **In-Flight Icing:** Supercooled water droplets freeze on wing leading edges, disrupting aerodynamic lift and increasing aircraft weight.
- Meteorological SIGMET advisories provide real-time flight path re-routing to bypass these hazardous storm cells.

### 3. Step-by-Step Option & Misconception Analysis:
- **Assertion (A) Evaluation:** True. Weather forecasting is a mandatory operational requirement for aviation flight planning.
- **Reason (R) Evaluation:** True. Atmospheric turbulence, icing, wind shear, and thunderstorms present direct mechanical and aerodynamic flight hazards.
- **Causal Connection:** Reason (R) explains why meteorological flight planning is non-negotiable for aviation safety.
- **Option A is correct.** Both Assertion and Reason are true, and Reason is the correct explanation of Assertion."""),

    11: ("A", """### 1. Scientific Principle & Global Data Assimilation in NWP:
Numerical Weather Prediction (NWP) models simulate the Earth's atmosphere as a single, globally coupled hydrodynamic continuum without artificial political boundaries.

### 2. Physical Process & Spatial Observational Continuity:
- The partial differential equations governing atmospheric mass, momentum, and energy conservation require continuous, uniform boundary conditions across the entire planetary surface.
- Unobserved data voids in vast geographic expanses—such as the Sahara, the Thar desert, the Southern Oceans, and polar ice sheets—act as blind spots where nascent atmospheric waves, pressure depressions, or heat lows can develop undetected.
- Establishing automated weather stations (AWS), drifting ocean buoys, and desert observatories eliminates these data gaps, providing the initial observations required for model initialization.

### 3. Step-by-Step Option & Misconception Analysis:
- **Assertion (A) Evaluation:** True. Installing meteorological stations in isolated deserts and ocean basins is critical for global weather models.
- **Reason (R) Evaluation:** True. Numerical models require comprehensive, gap-free initial observational boundary data across all geographic domains.
- **Causal Connection:** Reason (R) describes the computational requirement that necessitates Assertion (A).
- **Option A is correct.** Both Assertion and Reason are true, and Reason is the correct explanation of Assertion."""),

    12: ("A", """### 1. Scientific Principle & Urban Climatology & Microclimates:
Urbanization permanently replaces natural vegetative land cover with artificial anthropogenic materials, fundamentally altering the local surface energy budget.

### 2. Physical Process & The Urban Heat Island (UHI) Mechanism:
- Building materials such as asphalt, concrete, and brick possess high thermal conductivity and high volumetric heat capacity, absorbing and storing vast amounts of solar radiation during daytime and releasing it slowly at night.
- The removal of trees and vegetation drastically reduces cooling via **evapotranspiration**.
- Furthermore, anthropogenic heat emissions from vehicles, air conditioners, and industrial machinery combine with tall building canyons that trap longwave radiation, producing the **Urban Heat Island (UHI)** effect and altering local convective precipitation patterns.

### 3. Step-by-Step Option & Misconception Analysis:
- **Assertion (A) Evaluation:** True. Rapid urbanization alters local microclimates, elevating urban temperatures and modifying convective rainfall.
- **Reason (R) Evaluation:** True. Artificial pavements, reduced evapotranspiration, and anthropogenic waste heat trap solar thermal energy.
- **Causal Connection:** Reason (R) provides the physical energy balance explanation for Assertion (A).
- **Option A is correct.** Both Assertion and Reason are true, and Reason is the correct explanation of Assertion."""),

    13: ("A", """### 1. Scientific Principle & High-Performance Computing (HPC) in Meteorology:
Atmospheric modeling involves solving non-linear primitive equations derived from the laws of classical physics across three-dimensional spatial domains.

### 2. Physical Process & Computational Complexity:
- The atmosphere is discretized into a 3D grid containing millions of vertical and horizontal grid points spanning the globe.
- At every grid point and across fractional time steps (seconds to minutes), supercomputers must numerically integrate the primitive equations:
  - Conservation of Momentum (Navier-Stokes equations on a rotating sphere)
  - Conservation of Mass (Continuity equation)
  - Conservation of Energy (First law of thermodynamics)
  - Ideal Gas Law equation of state
- Processing petabytes of satellite radiance data and calculating physical parameterizations (cloud microphysics, radiative transfer) requires supercomputing architectures performing quadrillions of calculations per second (petaflops).

### 3. Step-by-Step Option & Misconception Analysis:
- **Assertion (A) Evaluation:** True. Dynamic NWP models require high-performance supercomputers (e.g., IMD's Pratyush and Mihir).
- **Reason (R) Evaluation:** True. Supercomputers are required to solve massive sets of non-linear hydrodynamic equations across millions of 3D atmospheric grid cells.
- **Causal Connection:** Reason (R) describes the exact computational challenge that necessitates supercomputers.
- **Option A is correct.** Both Assertion and Reason are true, and Reason is the correct explanation of Assertion."""),

    14: ("A", """### 1. Scientific Principle & Macroeconomic Agro-Meteorology:
In monsoon-dependent agrarian economies, seasonal rainfall distribution serves as a primary determinant of macroeconomic stability and rural livelihood security.

### 2. Physical Process & Macroeconomic Linkages:
- The Indian South-West monsoon replenishes major river basin reservoirs, recharges agricultural aquifers, and drives over \\(60\\%\\) of total annual food grain production.
- Plentiful monsoon rains sustain hydroelectric power generation, suppress agricultural inflation, stimulate rural demand for manufactured goods, and stabilize government fiscal budgets.
- Conversely, severe monsoon deficits cause rural distress and drop GDP growth, making reliable seasonal monsoon forecasting essential for national budgetary planning and food security reserves.

### 3. Step-by-Step Option & Misconception Analysis:
- **Assertion (A) Evaluation:** True. Accurate seasonal monsoon forecasts are vital for national economic forecasting and governance.
- **Reason (R) Evaluation:** True. Monsoon rainfall directly dictates food grain production, reservoir reserves, hydroelectric capacity, and rural purchasing power.
- **Causal Connection:** Reason (R) details the concrete socioeconomic dependencies that make Assertion (A) true.
- **Option A is correct.** Both Assertion and Reason are true, and Reason is the correct explanation of Assertion."""),

    15: ("A", """### 1. Scientific Principle & Forecast Temporal Hierarchy:
National meteorological agencies partition forecasts into distinct lead-time windows characterized by different underlying physical modeling techniques.

### 2. Physical Process & Temporal Scales:
- IMD and global meteorological agencies maintain a standardized three-tier forecasting hierarchy:
  1. **Short-range forecasts (up to 48 hours):** Highly detailed tactical predictions based on high-resolution NWP models, radar, and satellite nowcasting for daily public safety and aviation.
  2. **Medium-range forecasts (3 to 10 days):** Synoptic-scale guidance based on global ensemble NWP models used for agricultural sowing, irrigation, and flood preparation.
  3. **Long-range / Extended forecasts (beyond 10 days to seasonal):** Probabilistic statistical and coupled ocean-atmosphere climate models used for macro-level policy and drought management.

### 3. Step-by-Step Option & Misconception Analysis:
- **Assertion (A) Evaluation:** True. Meteorological services classify predictions into short-range, medium-range, and long-range tiers.
- **Reason (R) Evaluation:** True. Different temporal scales correspond to distinct societal decision-making requirements, from daily tactics to seasonal strategy.
- **Causal Connection:** Reason (R) explains why meteorological services maintain this structured temporal classification.
- **Option A is correct.** Both Assertion and Reason are true, and Reason is the correct explanation of Assertion.""")
}

for idx in range(0, 15):
    raw_q = raw_p1[idx]
    q_num = idx + 1
    ans_letter, sol = oar_sols[q_num]
    
    item = {
        "questionCode": raw_q['questionCode'],
        "type": "OAR",
        "text": raw_q['text'],
        "options": oar_options,
        "correctAnswer": ans_letter,
        "solution": sol
    }
    part1_enhanced.append(item)

print(f"Added {len(part1_enhanced)} OAR questions")

# Q16 to Q29 (OMC)
omc_data = {
    16: {
        "ans": ["Cloud cover and type", "Air temperature", "Barometric pressure"],
        "sol": """### 1. Scientific Principle & Primary Meteorological Elements:
Meteorological observatories routinely record fundamental atmospheric state variables that define weather and dictate thermodynamic equilibrium in the lower troposphere.

### 2. Physical Process & Atmospheric State Variables:
- Primary monitored elements include:
  - **Air temperature:** Measured continuously via shielded thermometers or resistance temperature detectors.
  - **Barometric pressure:** Recorded using mercury or digital aneroid barometers to identify pressure gradients.
  - **Cloud cover and cloud genus:** Observed visually or via ceilometers to determine radiative forcing and precipitation potential.
- In contrast, tectonic plate motion is a solid-Earth geological phenomenon occurring deep within the lithosphere over geological epochs (centimeters per year), tracked by geodetic GPS arrays rather than meteorological observatories.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct.** Cloud cover and cloud type are primary meteorological elements indicating humidity, vertical motion, and precipitation risk.
- **Option B is correct.** Ambient air temperature is the central thermodynamic variable tracked at all meteorological stations.
- **Option C is incorrect.** Plate tectonic velocity is a geophysical/geological parameter studied in seismology and geodesy, not meteorology.
- **Option D is correct.** Barometric atmospheric pressure is a foundational parameter used to map pressure fields and predict winds."""
    },
    17: {
        "ans": ["Agriculture and disaster management", "Marine navigation and fisheries", "Commercial aviation"],
        "sol": """### 1. Scientific Principle & Applied Meteorological Socio-Economics:
Accurate weather forecasting provides operational risk mitigation across human economic sectors exposed to the open atmospheric boundary layer.

### 2. Physical Process & Sector Vulnerabilities:
- **Agriculture:** Crop sowing, pesticide application, and harvesting schedules depend on rainfall timing to avoid crop ruin.
- **Marine Navigation & Fisheries:** Fishermen and cargo freighters require advance marine gales, wave height, and cyclone warnings to prevent capsizing.
- **Commercial Aviation:** Pilots require upper-air wind, turbulence, thunderstorm, and jet stream forecasts for flight safety and fuel efficiency.
- Deep subterranean speleology (cave exploration) occurs deep inside subterranean rock chambers where temperature and humidity remain constant year-round, completely isolated from surface weather.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct.** Agricultural operations and disaster management rely on weather forecasts for food security and life safety.
- **Option B is incorrect.** Deep cave exploration is sheltered from atmospheric weather by thick overlying rock strata.
- **Option C is correct.** Coastal fishing and commercial shipping depend on marine weather forecasts to navigate safely.
- **Option D is correct.** Aviation flight planning requires real-time weather forecasts to avoid hazardous turbulence and icing."""
    },
    18: {
        "ans": ["El Niño and La Niña events in the Pacific Ocean", "Snow cover extent over the Eurasian landmass", "Indian Ocean Dipole (IOD)"],
        "sol": """### 1. Scientific Principle & Teleconnections in Monsoon Dynamics:
The Indian summer monsoon is an planetary-scale circulation system influenced by regional thermal contrasts and global climate oscillations (**teleconnections**).

### 2. Physical Process & Climatological Teleconnections:
- **ENSO (El Niño/La Niña):** Anomalous warming in the central/eastern Pacific (El Niño) weakens the Walker circulation, frequently suppressing Indian monsoon rains, while La Niña supports strong monsoons.
- **Indian Ocean Dipole (IOD):** A positive IOD (warm western Indian Ocean) enhances moisture convergence toward the Indian subcontinent.
- **Eurasian Snow Cover:** Heavy winter/spring snow over Eurasia delays land warming and the northward migration of the monsoon trough, weakening the thermal gradient.
- Lunar phases and tidal cycles govern astronomical ocean tides, but have negligible thermodynamic impact on planetary monsoon circulations.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct.** Pacific ENSO conditions represent the primary global teleconnection modulating the Indian monsoon.
- **Option B is incorrect.** Lunar phases influence gravitational ocean tides, not atmospheric monsoon rainfall dynamics.
- **Option C is correct.** Eurasian snow cover governs the thermal contrast between the Asian landmass and the Indian Ocean.
- **Option D is correct.** The Indian Ocean Dipole directly alters sea surface temperature gradients and moisture flux over the Arabian Sea."""
    },
    19: {
        "ans": ["Maximum and minimum temperatures", "Relative humidity levels", "Isobars indicating high and low pressure regions"],
        "sol": """### 1. Scientific Principle & Synoptic Weather Cartography:
Newspaper weather maps published by the India Meteorological Department translate complex three-dimensional atmospheric datasets into standardized, accessible synoptic charts.

### 2. Physical Process & Cartographic Representation:
- Standard published synoptic elements include:
  - **Extreme Temperatures:** Daily maximum and minimum temperatures recorded over the preceding \\(24\\text{ hours}\\).
  - **Atmospheric Moisture:** Morning and evening relative humidity percentages.
  - **Pressure Fields:** Contoured isobars (lines of equal pressure) displaying high (H) and low (L) pressure cells, troughs, and cyclonic systems.
- Financial stock indices (e.g., Sensex, Nifty) are economic metrics completely outside the scientific purview of meteorological charts.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct.** Maximum and minimum daily temperatures are standard synoptic reporting elements.
- **Option B is correct.** Relative humidity levels are universally reported to indicate ambient air moisture.
- **Option C is incorrect.** Stock market trends are commercial economic indicators, not meteorological elements.
- **Option D is correct.** Isobars are fundamental cartographic features depicting horizontal pressure distributions."""
    },
    20: {
        "ans": ["Ambient air temperature", "Relative humidity", "Wind speed"],
        "sol": """### 1. Scientific Principle & Human Biometeorology & Thermal Comfort:
Human thermal comfort depends on the rate of heat exchange between the human body core and the ambient atmospheric environment.

### 2. Physical Process & Thermoregulation & Heat Index:
- The human body maintains homeostatic core temperature (\\(\\sim 37^\\circ\\text{C}\\)) by shedding metabolic heat via radiation, convection, and evaporative cooling (sweat evaporation).
- **Temperature & Humidity:** At high temperatures, high relative humidity impedes sweat evaporation (as air is near vapor saturation), creating a stifling, dangerous apparent temperature (Heat Index).
- **Wind Speed:** Moving air strips away the boundary layer of moist air adjacent to skin, accelerating evaporative cooling or convective heat loss (wind chill).
- Geomagnetic field strength is an imperceptible planetary magnetic force with zero impact on skin thermal balance.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect.** Geomagnetic field strength does not affect human skin heat loss or perceived comfort.
- **Option B is correct.** Ambient air temperature is the primary baseline variable governing convective heat transfer.
- **Option C is correct.** Relative humidity governs the rate of sweat evaporation from human skin.
- **Option D is correct.** Wind speed dictates the convective stripping of the skin's thermal boundary layer."""
    },
    21: {
        "ans": ["Intertropical Convergence Zone (ITCZ) seasonal shift", "Tibetan Plateau heating patterns", "Mascarene High pressure area intensity near Madagascar"],
        "sol": """### 1. Scientific Principle & South-West Monsoon Circulation Drivers:
The Asian monsoon circulation is an immense seasonal sea-breeze system driven by differential sensible and latent heating between the Asian continental landmass and the Indian Ocean.

### 2. Physical Process & Synoptic Drivers:
- **ITCZ Migration:** During boreal summer, the thermal equator shifts northward over the Indo-Gangetic plains (Monsoon Trough), pulling south-easterly trade winds across the equator where Coriolis force turns them into south-westerly monsoon winds.
- **Tibetan Plateau:** Elevated sensible heating acts as an elevated thermal heat engine, generating strong upper-tropospheric anticyclones and the Tropical Easterly Jet.
- **Mascarene High:** A semi-permanent high-pressure cell near Madagascar (\\(30^\\circ\\text{S}, 50^\\circ\\text{E}\\)) that drives the cross-equatorial Low-Level Jet (Findlater Jet) pumping moisture into India.
- Earth's core rotation is a deep geophysical constant with zero relevance to seasonal meteorological cycles.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct.** The seasonal northward migration of the ITCZ is the primary synoptic driver drawing the monsoon winds.
- **Option B is incorrect.** Earth's core rotation is a deep planetary constant that does not govern annual monsoon onset.
- **Option C is correct.** Sensible heating over the high Tibetan Plateau drives upper-level divergence and the monsoon engine.
- **Option D is correct.** The intensity of the Mascarene High dictates the velocity of the cross-equatorial monsoon wind flow."""
    },
    22: {
        "ans": ["Sea surface temperature gradients", "Atmospheric pressure oscillations", "Historical rainfall datasets across decades"],
        "sol": """### 1. Scientific Principle & Empirical & Statistical Climatology:
Statistical forecasting models rely on empirical mathematical relationships established over multi-decadal historical observations between global predictor indices and regional monsoon rainfall.

### 2. Physical Process & Predictive Covariates:
- Formulated originally by Sir Gilbert Walker, statistical models utilize stable oceanic and atmospheric predictors:
  - **Historical Rainfall Records:** Decadal datasets spanning \\(50\\text{--}100\\text{ years}\\) to train regression and machine learning algorithms.
  - **Sea Surface Temperature (SST) Gradients:** Equatorial Pacific (Niño-3.4) and Indian Ocean temperature anomalies.
  - **Atmospheric Pressure Oscillations:** Darwin-Tahiti pressure differences (Southern Oscillation Index) and North Atlantic Oscillation.
- Local volcanic rock composition is an invariant geological property that has no predictive value for seasonal climate variability.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct.** Ocean SST anomalies are primary boundary forcings used in statistical monsoon models.
- **Option B is correct.** Planetary atmospheric pressure oscillations (e.g., Southern Oscillation) serve as classical predictive inputs.
- **Option C is correct.** Long-term historical observational rainfall series are mandatory to calibrate statistical regression weights.
- **Option D is incorrect.** Volcanic mineral composition is an invariant lithological property unrelated to atmospheric dynamics."""
    },
    23: {
        "ans": ["Humidity", "Temperature", "Pressure"],
        "sol": """### 1. Scientific Principle & Thermodynamic State of the Atmosphere:
The physical state of the atmospheric fluid at any point in space and time is mathematically defined by thermodynamic state variables and dynamic motion vectors.

### 2. Physical Process & Equations of State:
- Classical atmospheric physics characterizes air parcels using fundamental state parameters linked by the Ideal Gas Law:
  \\[P = \\rho R_d T_v\\]
  where:
  - **Pressure (\\(P\\)):** The compressive weight of overlying air.
  - **Temperature (\\(T\\)):** The mean kinetic energy of gas molecules.
  - **Humidity (\\(q\\)):** The concentration of water vapor determining virtual temperature (\\(T_v\\)) and latent heat.
- Stellar magnitude is an astronomical measure of the apparent brightness of celestial stars, completely external to Earth's atmospheric state.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct.** Atmospheric humidity indicates the moisture content essential for cloud and precipitation dynamics.
- **Option B is correct.** Temperature represents the basic thermal state of the atmosphere.
- **Option C is incorrect.** Stellar magnitude is an astronomical measurement of celestial bodies, not a meteorological state variable.
- **Option D is correct.** Atmospheric pressure governs fluid motion and vertical atmospheric stability."""
    },
    24: {
        "ans": ["Upper-air radiosondes", "Doppler weather radars", "Geostationary and polar-orbiting satellites"],
        "sol": """### 1. Scientific Principle & Multi-Tier Meteorological Remote Sensing:
Accurate weather forecasting demands a continuous, integrated observing system capturing atmospheric parameters from the surface to the stratosphere.

### 2. Physical Process & Sensor Modalities:
- **Satellites (e.g., INSAT-3D, Kalpana):** Geostationary and polar-orbiting platforms capture real-time visible, infrared, and water-vapor radiances to track cloud motion and cyclone tracks.
- **Doppler Weather Radars (DWR):** Transmit microwave pulses to measure radar reflectivity (precipitation intensity) and Doppler frequency shift (wind speed and direction inside storms).
- **Radiosondes:** Sensor packages lofted by hydrogen balloons transmitting vertical profiles of pressure, temperature, and humidity.
- Seismographs detect elastic seismic body and surface waves propagating through the solid Earth lithosphere during earthquakes, not atmospheric weather.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect.** Seismograph arrays measure lithospheric tectonic earthquakes, not atmospheric weather elements.
- **Option B is correct.** Radiosondes provide essential vertical in-situ thermodynamic profiles of the upper atmosphere.
- **Option C is correct.** Doppler radars provide high-resolution real-time tracking of storms and precipitation wind velocities.
- **Option D is correct.** Meteorological satellites provide comprehensive global observation of cloud patterns and sea surface temperatures."""
    },
    25: {
        "ans": ["Radar reflectivity showing storm cell intensity", "Moisture convergence levels in lower troposphere", "Atmospheric instability indices"],
        "sol": """### 1. Scientific Principle & Severe Convective Storm Dynamics:
Severe thunderstorms and localized cloudbursts are mesoscale convective systems driven by buoyant instability, abundant boundary-layer moisture, and dynamic lifting triggers.

### 2. Physical Process & Convective Parameter Evaluation:
- **Atmospheric Instability Indices:** Metrics such as Convective Available Potential Energy (CAPE) and Lifted Index (LI) measure the buoyant energy available to accelerate rising air parcels.
- **Moisture Convergence:** Strong low-level convergence of water vapor replenishes the moisture required for continuous cloud condensation.
- **Radar Reflectivity:** High radar reflectivity factors (measured in dBZ, with values \\(> 50\\text{ dBZ}\\) indicating severe hail and torrential rain) track active storm cores in real time.
- Oceanic crust density is a static geophysical property of the lithosphere that does not influence short-term convective weather.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct.** Radar reflectivity (dBZ) directly indicates precipitation intensity and hail cores inside thunderstorms.
- **Option B is correct.** Low-level moisture convergence supplies the latent energy fueling convective storm updrafts.
- **Option C is correct.** Instability indices (e.g., CAPE) quantify the atmospheric potential for explosive convective updrafts.
- **Option D is incorrect.** Oceanic crustal density is a geological property that plays no role in atmospheric convective storm warnings."""
    },
    26: {
        "ans": ["Agricultural planning and seed procurement", "Disaster management preparedness for droughts or floods", "Water reservoir management and hydroelectric power generation"],
        "sol": """### 1. Scientific Principle & Climate Services & Long-Range Planning:
Seasonal and extended-range meteorological outlooks (spanning several months) provide strategic predictive intelligence for climate-sensitive macroeconomic sectors.

### 2. Physical Process & Strategic Sector Applications:
- **Agriculture:** Enables state agencies and farmers to decide crop choices (e.g., drought-tolerant millets versus water-intensive paddy) and procure appropriate seed varieties.
- **Water Resource Management:** Informs dam irrigation schedules, urban water rationing, and hydroelectric generation planning across river basins.
- **Disaster Preparedness:** Allows relief organizations and governments to preposition grain reserves, fodder camps, and flood evacuation equipment.
- Interior residential lighting design depends on building architectural aesthetics and room dimensions, not seasonal climate forecasts.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect.** Interior room lighting design is an indoor architectural concern unaffected by seasonal climate outlooks.
- **Option B is correct.** Agricultural planning relies heavily on seasonal forecasts to schedule sowing and seed distribution.
- **Option C is correct.** Disaster management authorities use seasonal outlooks to prepare contingency resources for floods or droughts.
- **Option D is correct.** Hydrological reservoir managers rely on seasonal rainfall projections to balance flood control and hydroelectric storage."""
    },
    27: {
        "ans": ["Soil moisture depletion levels", "Evapotranspiration rates driven by temperature and wind", "Cumulative rainfall deficit over specific crop growing phases"],
        "sol": """### 1. Scientific Principle & Agricultural Drought Quantification:
Agricultural drought occurs when soil moisture reserves fall below the critical threshold required to support normal plant growth and crop transpiration.

### 2. Physical Process & Hydro-Climatic Water Balance:
- Agricultural drought is evaluated via the soil water balance:
  - **Cumulative Rainfall Deficit:** Quantifying the shortfall of precipitation relative to long-term averages during critical crop phenological stages (e.g., flowering, grain filling).
  - **Evapotranspiration (ET):** High ambient temperatures, low humidity, and high winds accelerate water loss from both soil and plant stomata.
  - **Soil Moisture Depletion:** Root-zone soil moisture falling below the permanent wilting point leads to irreversible plant desiccation.
- International commodity market valuations of grains reflect speculative financial trading rather than the physical biological status of crops in fields.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct.** Depletion of root-zone soil moisture is the direct physical cause of agricultural drought stress.
- **Option B is incorrect.** Financial stock market valuations are economic metrics that do not measure physical agricultural drought.
- **Option C is correct.** High potential evapotranspiration driven by heat and dry winds accelerates crop water stress.
- **Option D is correct.** Cumulative rainfall deficits during sensitive growth phases determine the severity of agricultural drought."""
    },
    28: {
        "ans": ["Ambient temperature ranges", "Relative humidity and leaf wetness duration", "Recent rainfall amounts"],
        "sol": """### 1. Scientific Principle & Agro-Meteorological Plant Pathology:
The proliferation of agricultural fungal pathogens, bacterial blights, and insect pests is directly regulated by microclimatic conditions within the crop canopy.

### 2. Physical Process & Disease Triad & Microclimate:
- Fungal spores (e.g., rusts, powdery mildew, blast) and bacterial pathogens require specific environmental triggers to germinate and penetrate plant tissues:
  - **Leaf Wetness & Humidity:** Sustained relative humidity (\\(> 80\\%\\)) and liquid moisture on leaf surfaces are mandatory for fungal spore germination.
  - **Temperature:** Specific thermal windows (e.g., \\(20^\\circ\\text{C}\\text{--}28^\\circ\\text{C}\\)) maximize fungal mycelial growth and insect oviposition rates.
  - **Recent Rainfall:** Splashing raindrops mechanically disperse bacterial and fungal spores to adjacent healthy plants.
- Deep seismic tremors occur kilometers underground and have zero biological impact on crop canopy plant diseases.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct.** Temperature ranges determine the metabolic and reproductive rates of pests and plant pathogens.
- **Option B is incorrect.** Seismic tremor frequency relates to subterranean tectonic faults and has no effect on crop plant diseases.
- **Option C is correct.** High relative humidity and prolonged leaf wetness provide the essential moisture for fungal spore infection.
- **Option D is correct.** Recent rainfall provides moisture and facilitates the physical dissemination of pathogen spores."""
    },
    29: {
        "ans": ["Satellite radiance measurements", "Upper-air balloon soundings", "Surface station temperature and pressure readings"],
        "sol": """### 1. Scientific Principle & Data Assimilation in NWP:
Numerical Weather Prediction requires an accurate, dynamically consistent representation of the state of the atmosphere at initial time (\\(t = 0\\)), constructed via **data assimilation**.

### 2. Physical Process & Multi-Source Observational Fusion:
- Data assimilation schemes (such as 4D-Var) ingest billions of observations from disparate platforms:
  - **Surface Weather Stations:** Ground-level pressure, temperature, dew point, and wind velocity readings.
  - **Radiosonde Balloon Soundings:** In-situ vertical profiles of tropospheric and stratospheric parameters.
  - **Spaceborne Satellite Radiances:** Infrared and microwave radiances measuring atmospheric temperature and moisture soundings across oceans.
- Subterranean mineral assays evaluate underground ore and petroleum deposits, bearing zero relevance to atmospheric fluid dynamic initialization.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct.** Satellite radiance observations provide the vast majority of continuous data over oceans for NWP models.
- **Option B is correct.** Radiosonde balloon soundings supply critical, high-accuracy in-situ vertical profiles for model assimilation.
- **Option C is correct.** Surface station temperature and pressure readings anchor boundary-layer states in weather models.
- **Option D is incorrect.** Subterranean mineral assays assess geological deposits and are not used in atmospheric weather modeling."""
    }
}

for idx in range(15, 29):
    raw_q = raw_p1[idx]
    q_num = idx + 1
    data = omc_data[q_num]
    
    item = {
        "questionCode": raw_q['questionCode'],
        "type": "OMC",
        "text": raw_q['text'],
        "options": raw_q['options'],
        "correctAnswer": data['ans'],
        "solution": data['sol']
    }
    part1_enhanced.append(item)

print(f"Added OMC questions, total now: {len(part1_enhanced)}")

with open('scripts/ch9_p1_starter.json', 'w', encoding='utf-8') as f:
    json.dump(part1_enhanced, f, indent=2, ensure_ascii=False)

print("Saved first 29 questions to scripts/ch9_p1_starter.json")
