# -*- coding: utf-8 -*-
"""
Generator for MH-9-SCIT-9-9.1: Weather, Climate & Meteorology
40 Exam + 30 Practice + 12 Mock (with SVGs) = 82 Questions
"""
import json

TOPIC_CODE = "MH-9-SCIT-9-9.1"
OUTPUT_FILE = "scripts/ch9_topic1.json"

exam_data = [
    {
        "q": "What is the primary difference between weather and climate?",
        "options": [
            "Weather represents short-term atmospheric conditions, while climate is the long-term average over decades",
            "Weather only measures rainfall, while climate only measures temperature",
            "Weather never changes, while climate changes every hour",
            "Weather is measured globally, while climate is purely local"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Weather describes atmospheric conditions at a specific place and time (changing hourly or daily), whereas climate is the statistical average of weather conditions recorded over a long period (typically 30 years or more)."
    },
    {
        "q": "Which instrument is used by meteorologists to measure atmospheric pressure?",
        "options": ["Hygrometer", "Barometer", "Anemometer", "Pyrometer"],
        "ans": 1,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "A barometer measures atmospheric pressure, typically expressed in millibars (mb) or hectopascals (hPa)."
    },
    {
        "q": "In which year was the India Meteorological Department (IMD) established?",
        "options": ["1875", "1947", "1905", "1950"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "The India Meteorological Department (IMD) was established in 1875 by the Government of India, initially headquartered at Shimla."
    },
    {
        "q": "Where is the current principal headquarters of the India Meteorological Department (IMD) located?",
        "options": ["Pune", "New Delhi", "Kolkata", "Mumbai"],
        "ans": 1,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "While IMD maintains a major climate division and meteorological center in Pune, its overall administrative headquarters is located at Mausam Bhavan in New Delhi."
    },
    {
        "q": "Which meteorological instrument is specifically used to determine wind speed?",
        "options": ["Wind vane", "Anemometer", "Barometer", "Hygrometer"],
        "ans": 1,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "An anemometer measures wind speed, whereas a wind vane determines wind direction."
    },
    {
        "q": "What parameter is measured by a hygrometer in atmospheric studies?",
        "options": ["Solar insolation", "Relative humidity", "Atmospheric density", "Precipitation acidity"],
        "ans": 1,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "A hygrometer measures the amount of water vapor in the atmosphere, commonly expressed as relative humidity."
    },
    {
        "q": "Who was the first Director General of IMD who established the connection between snowfall in the Himalayas and the Indian monsoon in 1877?",
        "options": ["Sir Gilbert Walker", "H. F. Blanford", "Dr. Vasant Gowarikar", "Sir C. V. Raman"],
        "ans": 1,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "H. F. Blanford, the first Meteorological Reporter to the Government of India, made the pioneering monsoon forecast in 1877 based on Himalayan snowfall."
    },
    {
        "q": "Sir Gilbert Walker established which global atmospheric circulation concept that impacts monsoon patterns worldwide?",
        "options": ["Hadley Cell", "Walker Circulation / Southern Oscillation", "Coriolis deflection", "Rossby waves"],
        "ans": 1,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Sir Gilbert Walker identified planetary-scale pressure oscillations across the Pacific and Indian Oceans, now termed the Walker Circulation and Southern Oscillation (ENSO)."
    },
    {
        "q": "Which Indian scientist developed a multi-parameter parametric model using 16 worldwide climatic indicators to forecast the Indian monsoon in the late 1980s?",
        "options": ["Dr. Homi Bhabha", "Dr. Vasant Gowarikar", "Dr. A. P. J. Abdul Kalam", "Dr. Vikram Sarabhai"],
        "ans": 1,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Dr. Vasant Gowarikar headed the initiative that developed the 16-parameter monsoon forecasting model used extensively by the IMD from 1988 onwards."
    },
    {
        "q": "What type of monsoon forecasting model solves complex mathematical differential equations of fluid dynamics and thermodynamics using supercomputers?",
        "options": ["Mathematical / Numerical Model (Dynamic Model)", "Statistical Empirical Model", "Astrological Model", "Traditional Almanac Model"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "hard",
        "exp": "Numerical Weather Prediction (NWP) uses supercomputers to integrate non-linear equations of atmospheric motion, thermodynamics, and radiative transfer."
    },
    {
        "q": "Which geostationary satellite series operated by ISRO provides continuous meteorological imaging and infrared telemetry to the IMD?",
        "options": ["IRNSS", "INSAT and GSAT series (e.g. INSAT-3D/3DR)", "Cartosat", "AstroSat"],
        "ans": 1,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "INSAT-3D and INSAT-3DR geostationary satellites carry advanced meteorological imagers and atmospheric sounders dedicated to round-the-clock weather monitoring."
    },
    {
        "q": "What is the standard unit of atmospheric pressure widely used on synoptic weather maps?",
        "options": ["Joule", "Hectopascal (hPa) or millibar (mb)", "Newton per meter", "Watt per square meter"],
        "ans": 1,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Atmospheric pressure is reported in hectopascals (hPa) or millibars (mb), where 1 hPa = 1 mb = 100 Pascals."
    },
    {
        "q": "What are the lines joining points of equal atmospheric pressure on a weather map called?",
        "options": ["Isotherms", "Isobars", "Isohyets", "Isonephs"],
        "ans": 1,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Isobars are isolines connecting geographic locations that experience the same atmospheric pressure at a given time."
    },
    {
        "q": "What happens to atmospheric pressure as altitude increases above sea level?",
        "options": ["It increases exponentially", "It remains completely constant", "It decreases continuously because the overlying column of air diminishes", "It fluctuates randomly between zero and infinity"],
        "ans": 2,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "As elevation increases, the weight of the overlying air column decreases and air becomes less dense, causing atmospheric pressure to decrease progressively."
    },
    {
        "q": "Which ocean phenomenon characterized by periodic abnormal warming of surface waters in the central and eastern tropical Pacific suppresses Indian monsoon rainfall?",
        "options": ["La Nina", "El Nino", "Indian Ocean Dipole (positive)", "North Atlantic Drift"],
        "ans": 1,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "El Nino events (abnormal warming of equatorial Pacific waters) disrupt the Walker circulation and are historically correlated with deficient or drought-prone Indian monsoons."
    },
    {
        "q": "What color-coded alert is issued by the IMD when severe weather is imminent and authorities must 'Take Action'?",
        "options": ["Green", "Yellow", "Orange", "Red"],
        "ans": 3,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "IMD's 4-color warning scale uses: Green (No warning), Yellow (Watch/Be updated), Orange (Alert/Be prepared), and Red (Warning/Take action)."
    },
    {
        "q": "On a daily basis, at what time of day does relative humidity typically reach its maximum value under clear skies?",
        "options": ["Mid-afternoon (around 2:00 PM)", "Just before or around sunrise when temperature is lowest", "Midnight", "Exactly at solar noon"],
        "ans": 1,
        "type": "OSC",
        "difficulty": "hard",
        "exp": "Relative humidity depends inversely on air temperature. Near dawn, air temperature drops to its minimum, lowering the saturation vapor pressure and pushing relative humidity to its daily peak."
    },
    {
        "q": "Which Doppler Weather Radar (DWR) capability enables meteorologists to detect cyclones and track extreme rainfall in real time?",
        "options": [
            "Measuring radioactive decay in clouds",
            "Measuring microwave echo frequency shift to determine precipitation intensity and wind velocity",
            "Detecting seismic waves from tectonic plates",
            "Absorbing solar ultraviolet rays directly"
        ],
        "ans": 1,
        "type": "OSC",
        "difficulty": "hard",
        "exp": "Doppler radar measures the frequency shift (Doppler effect) of reflected electromagnetic pulses to determine both the radial velocity of raindrops/winds and the echo reflectivity."
    },
    {
        "q": "What is the primary driving mechanism of the Indian Southwest Monsoon winds?",
        "options": [
            "Centrifugal force of Earth's rotation alone",
            "Differential heating between the Indian subcontinent landmass and the surrounding Indian Ocean",
            "Gravitational pull of the Moon on surface air",
            "Continuous volcanic emissions in the Himalayas"
        ],
        "ans": 1,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Intense summer heating of the Asian/Indian landmass creates an intense thermal low-pressure trough, drawing moisture-laden winds from the high-pressure Indian Ocean."
    },
    {
        "q": "What is an isobaric weather pattern characterized by closely spaced isobars indicative of?",
        "options": ["Calm, still air with zero breeze", "A steep pressure gradient producing strong, gusty winds", "Extremely dense freezing fog", "Total absence of atmospheric moisture"],
        "ans": 1,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Closely spaced isobars represent a steep horizontal pressure gradient force, which accelerates air masses and generates strong winds."
    },
    {
        "q": "Select ALL elements that constitute daily weather:",
        "options": [
            "Atmospheric temperature",
            "Relative humidity",
            "Atmospheric pressure",
            "Speed of continental tectonic drift"
        ],
        "ans": [0, 1, 2],
        "type": "OMC",
        "difficulty": "easy",
        "exp": "Temperature, humidity, atmospheric pressure, wind, and precipitation are standard weather elements. Continental drift occurs over millions of years and is a geological process."
    },
    {
        "q": "Select ALL branches of the Indian Southwest Monsoon:",
        "options": [
            "Arabian Sea branch",
            "Bay of Bengal branch",
            "Arctic Ocean branch",
            "Mediterranean Sea branch"
        ],
        "ans": [0, 1],
        "type": "OMC",
        "difficulty": "easy",
        "exp": "The Southwest Monsoon splits around the southern tip of the Indian peninsula into the Arabian Sea branch and the Bay of Bengal branch."
    },
    {
        "q": "Select ALL services provided by the India Meteorological Department (IMD):",
        "options": [
            "Aviation weather forecasts for aircraft safety",
            "Agricultural advisories (Gramin Krishi Mausam Sewa)",
            "Early warning systems for tropical cyclones and tsunamis",
            "Stock exchange trading operations"
        ],
        "ans": [0, 1, 2],
        "type": "OMC",
        "difficulty": "easy",
        "exp": "IMD delivers vital public advisories including aviation forecasting, agromet bulletins for farmers, and disaster warnings for cyclones, storms, and tsunamis."
    },
    {
        "q": "True or False: Climate changes continuously on an hourly basis just like weather.",
        "options": ["True", "False"],
        "ans": 1,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "False. Weather fluctuates from hour to hour, but climate represents stable long-term statistical averages over at least 30 years."
    },
    {
        "q": "True or False: Anemometers measure wind direction while wind vanes measure wind speed.",
        "options": ["True", "False"],
        "ans": 1,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "False. Anemometers measure wind speed, while wind vanes indicate the compass direction from which the wind is blowing."
    },
    {
        "q": "True or False: Standard sea-level atmospheric pressure is approximately 1013.25 hPa (or 1 atm).",
        "options": ["True", "False"],
        "ans": 0,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "True. Standard mean sea level atmospheric pressure is officially defined as 1013.25 hPa (101.325 kPa or 760 mm of mercury)."
    },
    {
        "q": "True or False: In a tropical cyclone in the Northern Hemisphere, winds spiral inward in a counterclockwise direction around the central low pressure.",
        "options": ["True", "False"],
        "ans": 0,
        "type": "OTF",
        "difficulty": "medium",
        "exp": "True. Due to the Coriolis effect deflecting moving air to the right in the Northern Hemisphere, winds spiral counterclockwise into a low-pressure cyclone center."
    },
    {
        "q": "True or False: Statistical monsoon prediction models evaluate historical correlations among ocean-atmospheric parameters across past decades.",
        "options": ["True", "False"],
        "ans": 0,
        "type": "OTF",
        "difficulty": "medium",
        "exp": "True. Statistical models rely on empirical historical data and statistical regression between global precursors and Indian monsoon rainfall."
    },
    {
        "q": "Assertion (A): High-altitude hill stations like Mahabaleshwar and Shimla experience lower atmospheric pressure than coastal cities like Mumbai.\\nReason (R): As altitude increases, the height and density of the overlying atmospheric column decrease.",
        "options": [
            "Both A and R are true, and R is the correct explanation of A",
            "Both A and R are true, but R is not the correct explanation of A",
            "A is true, but R is false",
            "A is false, but R is true"
        ],
        "ans": 0,
        "type": "OAR",
        "difficulty": "medium",
        "exp": "Atmospheric pressure is the gravitational weight of air above a unit area. At higher elevations, less air resides above, resulting in lower barometric pressure."
    },
    {
        "q": "Assertion (A): Dew drops form on grass blades predominantly during clear, calm nights rather than cloudy nights.\\nReason (R): On clear nights, rapid terrestrial infrared radiation causes ground surfaces to cool below the dew point temperature of adjacent air.",
        "options": [
            "Both A and R are true, and R is the correct explanation of A",
            "Both A and R are true, but R is not the correct explanation of A",
            "A is true, but R is false",
            "A is false, but R is true"
        ],
        "ans": 0,
        "type": "OAR",
        "difficulty": "hard",
        "exp": "Clouds trap outgoing longwave radiation. On cloudless nights, unimpeded radiative cooling drops ground temperature below the dew point, condensing water vapor into dew."
    },
    {
        "q": "Assertion (A): Modern numerical weather prediction relies heavily on high-performance supercomputing clusters.\\nReason (R): Solving non-linear differential equations representing atmospheric dynamics across global three-dimensional grids requires billions of mathematical operations per second.",
        "options": [
            "Both A and R are true, and R is the correct explanation of A",
            "Both A and R are true, but R is not the correct explanation of A",
            "A is true, but R is false",
            "A is false, but R is true"
        ],
        "ans": 0,
        "type": "OAR",
        "difficulty": "medium",
        "exp": "Atmospheric models segment the globe into millions of 3D grid cells; computing real-time thermodynamic changes requires massive supercomputing power."
    },
    {
        "q": "Fill in the blank: The scientific study of the atmosphere and atmospheric phenomena, particularly for weather forecasting, is known as ________.",
        "options": ["meteorology", "seismology", "petrology", "geomorphology"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "easy",
        "exp": "Meteorology is the branch of atmospheric science focused on weather processes and short-to-medium-term forecasting."
    },
    {
        "q": "Fill in the blank: Standard atmospheric pressure at sea level supports a vertical column of mercury of exactly ________ mm.",
        "options": ["760", "1000", "500", "250"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "easy",
        "exp": "One standard atmosphere (1 atm) supports a column of mercury of 760 mm in a Torricellian barometer."
    },
    {
        "q": "Fill in the blank: The rainfall measuring instrument installed at standard meteorological stations is called a ________ gauge.",
        "options": ["rain", "pressure", "humidity", "wind"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "easy",
        "exp": "A rain gauge (udometer or pluviometer) collects and measures liquid precipitation over a given time interval."
    },
    {
        "q": "Fill in the blank: The seasonal reversal of prevailing wind directions accompanied by corresponding changes in precipitation is termed a ________.",
        "options": ["monsoon", "tornado", "typhoon", "blizzard"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "easy",
        "exp": "Monsoon (derived from the Arabic 'mausim' meaning season) refers to the seasonal shift in wind direction bringing heavy seasonal rains."
    },
    {
        "q": "Fill in the blank: The Indian supercomputer dedicated to high-resolution numerical weather prediction hosted at IITM Pune is named ________.",
        "options": ["Pratyush", "Aryabhata", "Rohini", "Saraswati"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "hard",
        "exp": "Pratyush (along with Mihir at NCMRWF) is a high-performance supercomputing facility dedicated to monsoon research and weather modeling in India."
    },
    {
        "q": "If sea level pressure is 1013 hPa and the pressure decreases at an average lapse rate of 12 hPa per 100 meters in the lower troposphere, what is the estimated pressure (in hPa) at an altitude of 1,000 meters?",
        "options": ["893", "900", "850", "950"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "medium",
        "exp": "At 1,000 m (10 intervals of 100 m), pressure drops by 10 * 12 = 120 hPa. Estimated pressure = 1013 - 120 = 893 hPa."
    },
    {
        "q": "According to the World Meteorological Organization (WMO), climate averages are calculated over a standard minimum baseline period of how many consecutive years?",
        "options": ["30", "10", "5", "50"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "easy",
        "exp": "The World Meteorological Organization (WMO) formally defines climatological standard normals as averages over consecutive 30-year periods."
    },
    {
        "q": "If a rain gauge collector has an opening of 200 cm^2 and collects 400 mL of rainwater during a 24-hour storm, what is the total rainfall depth recorded in millimeters? (Note: 1 mL = 1 cm^3; depth in cm = Volume / Area; 1 cm = 10 mm)",
        "options": ["20", "10", "40", "5"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "hard",
        "exp": "Depth in cm = 400 cm^3 / 200 cm^2 = 2 cm. Converting to millimeters: 2 * 10 = 20 mm."
    },
    {
        "q": "If the dry bulb temperature of air is 30 deg C and its actual vapor pressure is 21 hPa while its saturation vapor pressure at 30 deg C is 42 hPa, what is the relative humidity percentage?",
        "options": ["50", "25", "75", "100"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "easy",
        "exp": "Relative Humidity = (Actual Vapor Pressure / Saturation Vapor Pressure) * 100 = (21 / 42) * 100 = 50%."
    }
]

practice_data = [
    {
        "q": "Which atmospheric layer directly adjacent to Earth's surface contains virtually all weather phenomena including clouds, rain, and storms?",
        "options": ["Troposphere", "Stratosphere", "Mesosphere", "Thermosphere"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The troposphere extends from sea level up to 8-18 km altitude and contains about 75% of atmospheric mass and almost all water vapor, making it the theater of all weather."
    },
    {
        "q": "What term describes the temperature to which air must be cooled at constant pressure to become completely saturated with water vapor?",
        "options": ["Boiling point", "Dew point", "Critical point", "Absolute zero"],
        "ans": 1,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "The dew point is the temperature at which water vapor in air reaches 100% relative humidity and begins to condense into liquid droplets."
    },
    {
        "q": "Which type of clouds are commonly referred to as 'thunderheads' because they produce torrential rain, lightning, and hail?",
        "options": ["Cirrus", "Cumulonimbus", "Stratus", "Altocumulus"],
        "ans": 1,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Cumulonimbus clouds are towering vertical convective clouds capable of generating intense thunderstorms, violent squalls, and tornadoes."
    },
    {
        "q": "What is the primary factor causing winds to deflect to the right in the Northern Hemisphere and to the left in the Southern Hemisphere?",
        "options": ["Coriolis effect resulting from Earth's axial rotation", "Gravitational anomalies of ocean trenches", "Magnetic field lines of Earth", "Uneven tidal drag of the Moon"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "The Coriolis effect, caused by the rotation of the Earth on its axis, deflects moving air parcels to the right in the Northern Hemisphere and to the left in the Southern Hemisphere."
    },
    {
        "q": "What is the term for a prolonged period of abnormally low precipitation leading to severe water shortages and crop damage?",
        "options": ["Drought", "Flood", "Blizzard", "Cyclone"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "A drought is an extended duration of deficient precipitation relative to the statistical multi-year mean, causing hydrologic deficits."
    },
    {
        "q": "Which instrument uses a bimetallic strip or electrical resistance to continuously log temperature fluctuations onto a chart?",
        "options": ["Thermograph", "Barograph", "Anemometer", "Pluviometer"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "A thermograph provides a continuous graphical recording of atmospheric temperature over time."
    },
    {
        "q": "What does a sudden, sharp drop in barometric pressure typically indicate to a meteorologist?",
        "options": ["Clear, sunny skies and calm weather", "An approaching storm, low-pressure system, or squall", "A sudden rise in stratospheric ozone", "Total cessation of wind across the region"],
        "ans": 1,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "A rapid plunge in barometric pressure signals the rapid approach of a strong depression or cyclone, typically bringing gusty winds and heavy rain."
    },
    {
        "q": "Which organization is the specialized agency of the United Nations responsible for promoting international cooperation in atmospheric science and meteorology?",
        "options": ["WMO (World Meteorological Organization)", "WHO (World Health Organization)", "UNESCO", "UNEP"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The World Meteorological Organization (WMO), based in Geneva, coordinates worldwide meteorological observation and data exchange."
    },
    {
        "q": "What type of precipitation is formed when raindrops freeze into ice pellets while passing through a deep sub-freezing layer of air near the ground?",
        "options": ["Sleet", "Snow", "Drizzle", "Dew"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Sleet consists of translucent ice pellets formed when liquid raindrops freeze solid before reaching the surface."
    },
    {
        "q": "Which model approach compares current meteorological patterns with identical matching weather maps from past historical archives?",
        "options": ["Analogue / Statistical method", "Pure dynamic fluid modeling", "Chaos perturbation theory", "Astrological casting"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "hard",
        "exp": "The analogue method identifies past historical weather scenarios that closely resemble current conditions and assumes the atmosphere will evolve similarly."
    },
    {
        "q": "What is the calm, low-pressure center of a mature tropical cyclone called?",
        "options": ["The Eye", "The Eyewall", "The Spiral Band", "The Trough"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The eye is a roughly circular area of comparatively light winds, descending air currents, and clear-to-partly-cloudy skies situated at the vortex center of a tropical cyclone."
    },
    {
        "q": "What term describes the line on a weather map connecting points of equal atmospheric temperature?",
        "options": ["Isotherm", "Isobar", "Isohyet", "Isotach"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Isotherms are contour lines connecting locations experiencing equal temperature at a given time."
    },
    {
        "q": "Which wind belt dominates the tropical region between the equator and 30 degrees latitude in both hemispheres?",
        "options": ["Trade Winds (Easterlies)", "Prevailing Westerlies", "Polar Easterlies", "Jet Streams"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "The Trade Winds blow steadily from the subtropical high-pressure belts toward the equatorial doldrums (Intertropical Convergence Zone)."
    },
    {
        "q": "What is the boundary separating two distinct air masses of different temperatures and densities called?",
        "options": ["A front", "An isobar", "A ridge", "A solstice"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "A front (e.g. cold front, warm front, occluded front) is the transition zone between two contrasting air masses."
    },
    {
        "q": "Which meteorological term refers to the ratio of the actual amount of water vapor in air to the maximum amount the air can hold at that temperature?",
        "options": ["Relative humidity", "Absolute humidity", "Specific humidity", "Mixing ratio"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Relative humidity is the ratio (expressed as a percentage) of actual vapor pressure to the saturation vapor pressure at the prevailing temperature."
    },
    {
        "q": "Select ALL parameters tracked continuously by modern automatic weather stations (AWS):",
        "options": [
            "Solar radiation intensity",
            "Ambient air temperature and dew point",
            "Wind direction and gust speed",
            "Deep mantle radioactive composition"
        ],
        "ans": [0, 1, 2],
        "type": "OMC",
        "difficulty": "easy",
        "exp": "Automatic Weather Stations (AWS) log surface variables: radiation, temperature, dew point, wind velocity, and rainfall."
    },
    {
        "q": "Select ALL severe weather events monitored and forecasted by IMD:",
        "options": [
            "Tropical cyclones",
            "Heat waves and cold waves",
            "Heavy rainfall and cloudbursts",
            "Lunar solar eclipses"
        ],
        "ans": [0, 1, 2],
        "type": "OMC",
        "difficulty": "easy",
        "exp": "IMD forecasts meteorological disasters (cyclones, heatwaves, cloudbursts). Eclipses are astronomical occurrences computed by astrophysicists."
    },
    {
        "q": "Select ALL factors influencing regional climate:",
        "options": [
            "Latitude and angle of solar incidence",
            "Altitude above sea level",
            "Distance from the sea (continentality)",
            "Frequency of local municipal elections"
        ],
        "ans": [0, 1, 2],
        "type": "OMC",
        "difficulty": "easy",
        "exp": "Latitude, elevation, and proximity to large water bodies are primary geographical determinants of climate."
    },
    {
        "q": "True or False: The eye of a tropical cyclone contains the most violent winds and heaviest rainfall in the entire storm.",
        "options": ["True", "False"],
        "ans": 1,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "False. The eye is calm with light winds; the most destructive winds and heaviest rains reside in the eyewall directly surrounding the eye."
    },
    {
        "q": "True or False: Warm air can hold significantly more water vapor than cold air before reaching saturation.",
        "options": ["True", "False"],
        "ans": 0,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "True. The capacity of air to hold water vapor increases exponentially with temperature according to the Clausius-Clapeyron equation."
    },
    {
        "q": "True or False: An Orange alert from IMD instructs citizens and disaster agencies that disaster is ongoing and to 'Take Action' immediately.",
        "options": ["True", "False"],
        "ans": 1,
        "type": "OTF",
        "difficulty": "medium",
        "exp": "False. Orange means 'Be Prepared' (Alert). Red means 'Take Action' (Warning)."
    },
    {
        "q": "True or False: Monsoon onset over the Indian mainland typically commences over Kerala around June 1st.",
        "options": ["True", "False"],
        "ans": 0,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "True. The Southwest Monsoon normally hits the southern coast of Kerala around June 1st, marking the official onset over mainland India."
    },
    {
        "q": "Assertion (A): Coastal regions like Mumbai experience equable climates with modest diurnal temperature ranges.\\nReason (R): Water has a high specific heat capacity, heating and cooling much slower than adjacent continental landmasses.",
        "options": [
            "Both A and R are true, and R is the correct explanation of A",
            "Both A and R are true, but R is not the correct explanation of A",
            "A is true, but R is false",
            "A is false, but R is true"
        ],
        "ans": 0,
        "type": "OAR",
        "difficulty": "medium",
        "exp": "The high specific heat capacity of water moderates coastal climates through land and sea breezes, suppressing extreme temperature swings."
    },
    {
        "q": "Assertion (A): Air expands and rises when heated over an intense landmass.\\nReason (R): Heating increases molecular kinetic energy, lowering air density and establishing a localized low-pressure zone.",
        "options": [
            "Both A and R are true, and R is the correct explanation of A",
            "Both A and R are true, but R is not the correct explanation of A",
            "A is true, but R is false",
            "A is false, but R is true"
        ],
        "ans": 0,
        "type": "OAR",
        "difficulty": "medium",
        "exp": "Warm air expands, becomes less dense than surrounding cold air, and rises buoyantly, creating an atmospheric low pressure."
    },
    {
        "q": "Fill in the blank: The narrow bands of high-speed westerly winds meandering in the upper troposphere are called ________ streams.",
        "options": ["jet", "trade", "monsoon", "gust"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "medium",
        "exp": "Jet streams are fast, narrow air currents circulating in the tropopause at altitudes of 9 to 16 km."
    },
    {
        "q": "Fill in the blank: The side of a mountain range that faces incoming moisture-bearing winds and receives heavy rainfall is called the ________ slope.",
        "options": ["windward", "leeward", "downwind", "shadow"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "easy",
        "exp": "The windward slope forces air to rise, cool, and condense, yielding orographic precipitation."
    },
    {
        "q": "Fill in the blank: The dry region on the sheltered side of a mountain barrier that receives scanty rainfall is called the rain-________ zone.",
        "options": ["shadow", "basin", "forest", "divide"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "easy",
        "exp": "The rain-shadow zone (leeward side) experiences descending, warming air that inhibits condensation and rainfall."
    },
    {
        "q": "Fill in the blank: The color code assigned by IMD to indicate 'No Warning' (normal weather expected) is ________.",
        "options": ["Green", "Yellow", "Orange", "Red"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "easy",
        "exp": "Green signifies all clear with no severe adverse weather conditions anticipated."
    },
    {
        "q": "If an anemometer rotates at 120 revolutions per minute and each revolution corresponds to a wind travel distance of 1.5 meters, what is the wind speed in meters per second (m/s)?",
        "options": ["3", "1.5", "6", "12"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "medium",
        "exp": "Total distance per minute = 120 * 1.5 = 180 m. Wind speed in m/s = 180 / 60 = 3 m/s."
    },
    {
        "q": "If a city receives 120 mm of rainfall in June, 350 mm in July, 280 mm in August, and 150 mm in September, what is the total southwest monsoon seasonal rainfall in millimeters?",
        "options": ["900", "800", "1000", "950"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "easy",
        "exp": "Total = 120 + 350 + 280 + 150 = 900 mm."
    }
]

svg_diagrams = [
    # SVG 1: Meteorological instruments
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Standard Meteorological Instruments</text>
  <!-- Barometer -->
  <g transform="translate(30, 45)">
    <rect x="0" y="0" width="95" height="150" rx="8" fill="#1e293b" stroke="#38bdf8"/>
    <circle cx="47" cy="45" r="30" fill="#334155" stroke="#38bdf8" stroke-width="2"/>
    <line x1="47" y1="45" x2="62" y2="35" stroke="#f43f5e" stroke-width="2"/>
    <text x="47" y="105" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Barometer</text>
    <text x="47" y="125" fill="#94a3b8" font-size="9" text-anchor="middle">Atmospheric</text>
    <text x="47" y="137" fill="#94a3b8" font-size="9" text-anchor="middle">Pressure (hPa)</text>
  </g>
  <!-- Anemometer -->
  <g transform="translate(145, 45)">
    <rect x="0" y="0" width="95" height="150" rx="8" fill="#1e293b" stroke="#10b981"/>
    <line x1="47" y1="25" x2="47" y2="75" stroke="#94a3b8" stroke-width="3"/>
    <circle cx="25" cy="35" r="8" fill="#10b981"/>
    <circle cx="70" cy="35" r="8" fill="#10b981"/>
    <text x="47" y="105" fill="#10b981" font-size="11" font-weight="bold" text-anchor="middle">Anemometer</text>
    <text x="47" y="125" fill="#94a3b8" font-size="9" text-anchor="middle">Wind Speed</text>
    <text x="47" y="137" fill="#94a3b8" font-size="9" text-anchor="middle">(m/s or knots)</text>
  </g>
  <!-- Hygrometer -->
  <g transform="translate(260, 45)">
    <rect x="0" y="0" width="95" height="150" rx="8" fill="#1e293b" stroke="#fbbf24"/>
    <rect x="35" y="25" width="25" height="55" rx="5" fill="#334155"/>
    <line x1="47" y1="35" x2="47" y2="70" stroke="#f43f5e" stroke-width="2"/>
    <text x="47" y="105" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle">Hygrometer</text>
    <text x="47" y="125" fill="#94a3b8" font-size="9" text-anchor="middle">Relative</text>
    <text x="47" y="137" fill="#94a3b8" font-size="9" text-anchor="middle">Humidity (%)</text>
  </g>
  <!-- Rain Gauge -->
  <g transform="translate(375, 45)">
    <rect x="0" y="0" width="95" height="150" rx="8" fill="#1e293b" stroke="#f43f5e"/>
    <path d="M 30 25 L 65 25 L 55 60 L 40 60 Z" fill="#334155" stroke="#94a3b8"/>
    <rect x="42" y="60" width="12" height="25" fill="#0284c7"/>
    <text x="47" y="105" fill="#f43f5e" font-size="11" font-weight="bold" text-anchor="middle">Rain Gauge</text>
    <text x="47" y="125" fill="#94a3b8" font-size="9" text-anchor="middle">Precipitation</text>
    <text x="47" y="137" fill="#94a3b8" font-size="9" text-anchor="middle">Depth (mm)</text>
  </g>
</svg>''',

    # SVG 2: Weather vs Climate Table
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Weather vs Climate: Fundamental Distinctions</text>
  <!-- Table Header -->
  <rect x="25" y="45" width="450" height="30" fill="#334155" rx="4"/>
  <text x="135" y="65" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Weather</text>
  <text x="365" y="65" fill="#10b981" font-size="12" font-weight="bold" text-anchor="middle">Climate</text>
  <!-- Row 1: Duration -->
  <rect x="25" y="80" width="450" height="35" fill="#1e293b"/>
  <text x="135" y="102" fill="#f8fafc" font-size="11" text-anchor="middle">Short-term (hours to days)</text>
  <text x="365" y="102" fill="#f8fafc" font-size="11" text-anchor="middle">Long-term average (30+ years)</text>
  <!-- Row 2: Variability -->
  <rect x="25" y="120" width="450" height="35" fill="#1e293b"/>
  <text x="135" y="142" fill="#f8fafc" font-size="11" text-anchor="middle">Changes frequently &amp; rapidly</text>
  <text x="365" y="142" fill="#f8fafc" font-size="11" text-anchor="middle">Relatively stable over time</text>
  <!-- Row 3: Domain -->
  <rect x="25" y="160" width="450" height="40" fill="#1e293b"/>
  <text x="135" y="185" fill="#f8fafc" font-size="11" text-anchor="middle">Localized to a city or district</text>
  <text x="365" y="185" fill="#f8fafc" font-size="11" text-anchor="middle">Encompasses large geographical zones</text>
</svg>''',

    # SVG 3: Pressure vs Altitude
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Atmospheric Pressure vs Altitude Profile</text>
  <!-- Axes -->
  <line x1="70" y1="190" x2="450" y2="190" stroke="#64748b" stroke-width="2"/>
  <line x1="70" y1="40" x2="70" y2="190" stroke="#64748b" stroke-width="2"/>
  <text x="260" y="215" fill="#94a3b8" font-size="11" text-anchor="middle">Atmospheric Pressure (hPa)</text>
  <text x="25" y="115" fill="#94a3b8" font-size="11" transform="rotate(-90 25,115)" text-anchor="middle">Altitude (km)</text>
  <!-- Curve: Pressure decreases with altitude -->
  <path d="M 420 185 Q 260 170 160 120 T 90 50" fill="none" stroke="#38bdf8" stroke-width="3"/>
  <!-- Key labels -->
  <circle cx="420" cy="185" r="4" fill="#10b981"/>
  <text x="420" y="172" fill="#10b981" font-size="10" text-anchor="middle">Sea Level: 1013 hPa</text>
  <circle cx="210" cy="140" r="4" fill="#fbbf24"/>
  <text x="255" y="135" fill="#fbbf24" font-size="10">5.5 km: ~500 hPa (Half 1 atm)</text>
  <circle cx="105" cy="65" r="4" fill="#f43f5e"/>
  <text x="145" y="65" fill="#f43f5e" font-size="10">Mount Everest (8.8 km): ~300 hPa</text>
</svg>''',

    # SVG 4: IMD Cyclone Radar
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Doppler Weather Radar: Tropical Cyclone Spiral in Bay of Bengal</text>
  <!-- Concentric radar circles -->
  <circle cx="250" cy="130" r="90" fill="none" stroke="#334155" stroke-width="1"/>
  <circle cx="250" cy="130" r="60" fill="none" stroke="#334155" stroke-width="1"/>
  <circle cx="250" cy="130" r="30" fill="none" stroke="#334155" stroke-width="1"/>
  <!-- Crosshairs -->
  <line x1="150" y1="130" x2="350" y2="130" stroke="#334155"/>
  <line x1="250" y1="35" x2="250" y2="225" stroke="#334155"/>
  <!-- Spiral rainbands -->
  <path d="M 250 130 Q 280 100 290 60" fill="none" stroke="#ef4444" stroke-width="5"/>
  <path d="M 250 130 Q 220 160 190 190" fill="none" stroke="#f59e0b" stroke-width="4"/>
  <path d="M 250 130 Q 210 100 170 80" fill="none" stroke="#10b981" stroke-width="3"/>
  <!-- Eye -->
  <circle cx="250" cy="130" r="10" fill="#0f172a" stroke="#f8fafc" stroke-width="2"/>
  <text x="250" y="134" fill="#f8fafc" font-size="9" font-weight="bold" text-anchor="middle">EYE</text>
  <!-- Labels -->
  <text x="360" y="75" fill="#ef4444" font-size="11" font-weight="bold">Severe Eyewall</text>
  <text x="360" y="90" fill="#94a3b8" font-size="9">&gt; 120 km/h winds</text>
  <text x="80" y="180" fill="#38bdf8" font-size="10">Counterclockwise Spiral</text>
  <text x="80" y="195" fill="#94a3b8" font-size="9">(Northern Hemisphere)</text>
</svg>''',

    # SVG 5: Southwest Monsoon trajectory
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Southwest Monsoon Branches Across India</text>
  <!-- Stylized Indian Peninsular coastline -->
  <path d="M 200 45 L 250 140 L 300 45" fill="none" stroke="#64748b" stroke-width="2"/>
  <!-- Arabian Sea Branch (Left) -->
  <path d="M 120 180 Q 160 150 195 110" fill="none" stroke="#38bdf8" stroke-width="3"/>
  <polygon points="195,110 185,115 190,123" fill="#38bdf8"/>
  <text x="120" y="140" fill="#38bdf8" font-size="11" font-weight="bold">Arabian Sea Branch</text>
  <text x="120" y="155" fill="#94a3b8" font-size="9">Strikes Western Ghats</text>
  <!-- Bay of Bengal Branch (Right) -->
  <path d="M 360 180 Q 320 140 280 90" fill="none" stroke="#10b981" stroke-width="3"/>
  <polygon points="280,90 283,100 292,95" fill="#10b981"/>
  <text x="340" y="140" fill="#10b981" font-size="11" font-weight="bold">Bay of Bengal Branch</text>
  <text x="340" y="155" fill="#94a3b8" font-size="9">Heads toward Northeast</text>
  <!-- Low pressure trough -->
  <ellipse cx="250" cy="70" rx="35" ry="15" fill="#f43f5e" fill-opacity="0.3" stroke="#f43f5e"/>
  <text x="250" y="74" fill="#fca5a5" font-size="10" font-weight="bold" text-anchor="middle">Thermal Low</text>
</svg>''',

    # SVG 6: Walker Circulation & El Nino
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Equatorial Pacific Walker Circulation (Normal vs El Ni&#241;o)</text>
  <!-- Normal Walker Circulation Panel -->
  <g transform="translate(30, 45)">
    <rect x="0" y="0" width="205" height="165" rx="8" fill="#1e293b" stroke="#10b981"/>
    <text x="102" y="22" fill="#10b981" font-size="12" font-weight="bold" text-anchor="middle">Normal / La Ni&#241;a</text>
    <text x="20" y="55" fill="#38bdf8" font-size="10">Warm Pool: West Pacific</text>
    <text x="20" y="75" fill="#f8fafc" font-size="10">Strong Easterly Trade Winds</text>
    <text x="20" y="95" fill="#f8fafc" font-size="10">Vigorous Indian Monsoon</text>
    <rect x="15" y="115" width="175" height="30" rx="4" fill="#065f46"/>
    <text x="102" y="135" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle">Favorable Rainfall</text>
  </g>
  <!-- El Nino Panel -->
  <g transform="translate(265, 45)">
    <rect x="0" y="0" width="205" height="165" rx="8" fill="#1e293b" stroke="#ef4444"/>
    <text x="102" y="22" fill="#ef4444" font-size="12" font-weight="bold" text-anchor="middle">El Ni&#241;o Event</text>
    <text x="20" y="55" fill="#fbbf24" font-size="10">Warm Pool: Shifts Eastward</text>
    <text x="20" y="75" fill="#f8fafc" font-size="10">Trade Winds Weaken/Reverse</text>
    <text x="20" y="95" fill="#f8fafc" font-size="10">Disrupts Monsoon Flow</text>
    <rect x="15" y="115" width="175" height="30" rx="4" fill="#991b1b"/>
    <text x="102" y="135" fill="#fca5a5" font-size="11" font-weight="bold" text-anchor="middle">Risk of Drought / Deficit</text>
  </g>
</svg>''',

    # SVG 7: Maximum-Minimum Thermometer
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Six's Maximum and Minimum Thermometer</text>
  <!-- U-tube -->
  <path d="M 210 50 L 210 160 Q 210 185 250 185 Q 290 185 290 160 L 290 50" fill="none" stroke="#94a3b8" stroke-width="12"/>
  <!-- Mercury column in bend -->
  <path d="M 210 120 L 210 160 Q 210 185 250 185 Q 290 185 290 160 L 290 130" fill="none" stroke="#e2e8f0" stroke-width="8"/>
  <!-- Left arm: Minimum -->
  <text x="175" y="60" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="end">Minimum Scale</text>
  <line x1="180" y1="95" x2="204" y2="95" stroke="#38bdf8" stroke-width="2"/>
  <text x="175" y="100" fill="#38bdf8" font-size="10" text-anchor="end">Min Index</text>
  <!-- Right arm: Maximum -->
  <text x="325" y="60" fill="#ef4444" font-size="11" font-weight="bold">Maximum Scale</text>
  <line x1="296" y1="110" x2="320" y2="110" stroke="#ef4444" stroke-width="2"/>
  <text x="325" y="115" fill="#ef4444" font-size="10">Max Index</text>
  <!-- Caption -->
  <text x="250" y="215" fill="#f8fafc" font-size="11" text-anchor="middle">Records daily thermal extremes over a 24-hour cycle</text>
</svg>''',

    # SVG 8: Relative Humidity vs Temperature Cycle
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Diurnal Inversion: Relative Humidity vs Temperature</text>
  <!-- Axes -->
  <line x1="60" y1="190" x2="450" y2="190" stroke="#64748b" stroke-width="2"/>
  <line x1="60" y1="45" x2="60" y2="190" stroke="#64748b" stroke-width="2"/>
  <text x="250" y="215" fill="#94a3b8" font-size="11" text-anchor="middle">Time of Day (Midnight - Dawn - Noon - Sunset - Midnight)</text>
  <!-- Temperature curve (peaks at 2 PM) -->
  <path d="M 60 160 Q 150 175 250 80 T 440 160" fill="none" stroke="#ef4444" stroke-width="3"/>
  <text x="360" y="75" fill="#ef4444" font-size="11" font-weight="bold">Temperature (&#176;C)</text>
  <!-- Relative humidity curve (peaks at dawn) -->
  <path d="M 60 80 Q 150 65 250 160 T 440 80" fill="none" stroke="#38bdf8" stroke-width="3"/>
  <text x="120" y="60" fill="#38bdf8" font-size="11" font-weight="bold">Relative Humidity (%)</text>
  <!-- Dawn highlight -->
  <line x1="150" y1="50" x2="150" y2="190" stroke="#fbbf24" stroke-dasharray="3"/>
  <text x="150" y="42" fill="#fbbf24" font-size="10" font-weight="bold" text-anchor="middle">Dawn: Max RH</text>
</svg>''',

    # SVG 9: Synoptic Weather Map
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Synoptic Weather Chart: Isobars &amp; Pressure Centers</text>
  <!-- Low pressure center -->
  <ellipse cx="160" cy="120" rx="40" ry="25" fill="none" stroke="#ef4444" stroke-width="2"/>
  <ellipse cx="160" cy="120" rx="70" ry="45" fill="none" stroke="#ef4444" stroke-width="1.5"/>
  <ellipse cx="160" cy="120" rx="100" ry="65" fill="none" stroke="#ef4444" stroke-width="1"/>
  <text x="160" y="125" fill="#ef4444" font-size="16" font-weight="bold" text-anchor="middle">L (996)</text>
  <text x="160" y="175" fill="#fca5a5" font-size="9" text-anchor="middle">1000 hPa</text>
  <text x="160" y="195" fill="#fca5a5" font-size="9" text-anchor="middle">1004 hPa</text>
  <!-- High pressure center -->
  <ellipse cx="370" cy="120" rx="45" ry="30" fill="none" stroke="#38bdf8" stroke-width="2"/>
  <ellipse cx="370" cy="120" rx="80" ry="55" fill="none" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="370" y="125" fill="#38bdf8" font-size="16" font-weight="bold" text-anchor="middle">H (1024)</text>
  <text x="370" y="185" fill="#93c5fd" font-size="9" text-anchor="middle">1020 hPa</text>
  <!-- Wind arrow from High to Low -->
  <path d="M 320 120 L 240 120" stroke="#fbbf24" stroke-width="3" marker-end="url(#arr)"/>
  <text x="280" y="110" fill="#fbbf24" font-size="10" font-weight="bold" text-anchor="middle">Wind Flow</text>
</svg>''',

    # SVG 10: Numerical Weather Prediction Workflow
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Numerical Weather Prediction (NWP) Architecture</text>
  <!-- Step 1: Data Collection -->
  <g transform="translate(20, 50)">
    <rect x="0" y="0" width="95" height="120" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="47" y="25" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">1. Input Data</text>
    <text x="47" y="50" fill="#f8fafc" font-size="9" text-anchor="middle">Satellites, Radars,</text>
    <text x="47" y="65" fill="#f8fafc" font-size="9" text-anchor="middle">Weather Buoys,</text>
    <text x="47" y="80" fill="#f8fafc" font-size="9" text-anchor="middle">AWS Stations</text>
  </g>
  <!-- Arrow -->
  <path d="M 120 110 L 140 110" stroke="#f8fafc" stroke-width="2"/>
  <!-- Step 2: Quality Control & Assimilation -->
  <g transform="translate(145, 50)">
    <rect x="0" y="0" width="95" height="120" rx="6" fill="#1e293b" stroke="#10b981"/>
    <text x="47" y="25" fill="#10b981" font-size="11" font-weight="bold" text-anchor="middle">2. Assimilation</text>
    <text x="47" y="50" fill="#f8fafc" font-size="9" text-anchor="middle">3D Grid Mapping</text>
    <text x="47" y="65" fill="#f8fafc" font-size="9" text-anchor="middle">Quality filtering</text>
    <text x="47" y="80" fill="#f8fafc" font-size="9" text-anchor="middle">Initial State</text>
  </g>
  <!-- Arrow -->
  <path d="M 245 110 L 265 110" stroke="#f8fafc" stroke-width="2"/>
  <!-- Step 3: Supercomputer Model -->
  <g transform="translate(270, 50)">
    <rect x="0" y="0" width="95" height="120" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="47" y="25" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle">3. Computation</text>
    <text x="47" y="50" fill="#f8fafc" font-size="9" text-anchor="middle">Pratyush / Mihir</text>
    <text x="47" y="65" fill="#f8fafc" font-size="9" text-anchor="middle">Fluid Dynamics</text>
    <text x="47" y="80" fill="#f8fafc" font-size="9" text-anchor="middle">Thermodynamics</text>
  </g>
  <!-- Arrow -->
  <path d="M 370 110 L 390 110" stroke="#f8fafc" stroke-width="2"/>
  <!-- Step 4: Dissemination -->
  <g transform="translate(395, 50)">
    <rect x="0" y="0" width="85" height="120" rx="6" fill="#1e293b" stroke="#f43f5e"/>
    <text x="42" y="25" fill="#f43f5e" font-size="11" font-weight="bold" text-anchor="middle">4. Forecast</text>
    <text x="42" y="50" fill="#f8fafc" font-size="9" text-anchor="middle">Farmer SMS,</text>
    <text x="42" y="65" fill="#f8fafc" font-size="9" text-anchor="middle">Aviation Alert,</text>
    <text x="42" y="80" fill="#f8fafc" font-size="9" text-anchor="middle">Cyclone Warning</text>
  </g>
</svg>''',

    # SVG 11: IMD Cyclone Warning Scale
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">IMD 4-Stage Color Coded Weather Alert System</text>
  <!-- Green -->
  <rect x="30" y="45" width="100" height="150" rx="8" fill="#14532d" stroke="#22c55e"/>
  <text x="80" y="75" fill="#86efac" font-size="13" font-weight="bold" text-anchor="middle">GREEN</text>
  <text x="80" y="105" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">No Warning</text>
  <text x="80" y="130" fill="#dcfce7" font-size="9" text-anchor="middle">Normal weather</text>
  <!-- Yellow -->
  <rect x="145" y="45" width="100" height="150" rx="8" fill="#713f12" stroke="#eab308"/>
  <text x="195" y="75" fill="#fde047" font-size="13" font-weight="bold" text-anchor="middle">YELLOW</text>
  <text x="195" y="105" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">Watch</text>
  <text x="195" y="130" fill="#fef9c3" font-size="9" text-anchor="middle">Be updated</text>
  <!-- Orange -->
  <rect x="260" y="45" width="100" height="150" rx="8" fill="#7c2d12" stroke="#f97316"/>
  <text x="310" y="75" fill="#fdba74" font-size="13" font-weight="bold" text-anchor="middle">ORANGE</text>
  <text x="310" y="105" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">Alert</text>
  <text x="310" y="130" fill="#ffedd5" font-size="9" text-anchor="middle">Be prepared</text>
  <!-- Red -->
  <rect x="375" y="45" width="100" height="150" rx="8" fill="#7f1d1d" stroke="#ef4444"/>
  <text x="425" y="75" fill="#fca5a5" font-size="13" font-weight="bold" text-anchor="middle">RED</text>
  <text x="425" y="105" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">Warning</text>
  <text x="425" y="130" fill="#fee2e2" font-size="9" text-anchor="middle">Take action!</text>
</svg>''',

    # SVG 12: Orographic Precipitation
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Orographic Precipitation &amp; Rain-Shadow Effect</text>
  <!-- Mountain profile -->
  <path d="M 50 190 L 220 70 L 320 190" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
  <!-- Windward Side (Left) -->
  <path d="M 60 160 Q 120 130 180 80" fill="none" stroke="#38bdf8" stroke-width="3"/>
  <!-- Clouds & Rain on Windward -->
  <ellipse cx="180" cy="65" rx="30" ry="15" fill="#64748b"/>
  <ellipse cx="205" cy="60" rx="25" ry="15" fill="#94a3b8"/>
  <line x1="170" y1="85" x2="160" y2="115" stroke="#38bdf8" stroke-dasharray="2"/>
  <line x1="185" y1="85" x2="175" y2="115" stroke="#38bdf8" stroke-dasharray="2"/>
  <line x1="200" y1="85" x2="190" y2="115" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="2"/>
  <text x="100" y="90" fill="#38bdf8" font-size="11" font-weight="bold">Windward Slope</text>
  <text x="100" y="105" fill="#f8fafc" font-size="9">Rising air cools &#8594; Heavy rain</text>
  <!-- Leeward Side (Right) -->
  <path d="M 240 85 Q 290 130 350 160" fill="none" stroke="#f59e0b" stroke-width="3"/>
  <text x="350" y="100" fill="#f59e0b" font-size="11" font-weight="bold">Leeward Slope</text>
  <text x="350" y="115" fill="#fde68a" font-size="9">Rain-Shadow Zone</text>
  <text x="350" y="130" fill="#94a3b8" font-size="9">Descending air warms &#8594; Dry</text>
</svg>'''
]

mock_questions = [
    {
        "q": "Based on the meteorological instruments panel, which instrument is used specifically to measure the percentage of relative humidity in air?",
        "options": ["Hygrometer", "Barometer", "Anemometer", "Rain Gauge"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "As displayed in the panel, the hygrometer records relative humidity (%), whereas the barometer records atmospheric pressure, the anemometer wind speed, and the rain gauge rainfall depth."
    },
    {
        "q": "Referring to the Weather vs Climate distinction chart, which feature accurately characterizes climate rather than weather?",
        "options": [
            "Statistical average calculated over 30 or more consecutive years",
            "Fluctuates rapidly from hour to hour within a single afternoon",
            "Measured exclusively during sudden convective storms",
            "Applies strictly to a 10-meter radius around an individual building"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The comparison table indicates that climate reflects long-term statistical trends and averages over 30+ years, while weather denotes short-term, rapidly shifting localized conditions."
    },
    {
        "q": "Based on the barometric pressure versus altitude curve, what is the approximate atmospheric pressure at Mount Everest's summit (approx. 8.8 km above sea level)?",
        "options": ["Around 300 hPa (less than one-third of sea-level pressure)", "Exactly 1013 hPa", "Above 1500 hPa", "Zero hPa"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "The graph shows that at an altitude of approximately 8.8 km, atmospheric pressure drops steeply to around 300 hPa due to the reduced mass of the overlying air column."
    },
    {
        "q": "According to the Doppler radar display of a tropical cyclone in the Bay of Bengal, where are the strongest winds and heaviest convective precipitation concentrated?",
        "options": [
            "In the eyewall immediately encircling the central eye",
            "In the calm center of the eye itself",
            "Exclusively outside the radar coverage range",
            "Evenly distributed across the entire hemisphere"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "The radar scan highlights the eyewall—the intense red band surrounding the calm eye—as the zone possessing the most dangerous hurricane-force winds and maximum rain rates."
    },
    {
        "q": "Examining the map of Southwest Monsoon branches, which major mountain barrier intercepts the Arabian Sea branch causing copious precipitation along the western coast of Maharashtra?",
        "options": [
            "The Western Ghats (Sahyadri mountain range)",
            "The Aravalli Range",
            "The Vindhya Range",
            "The Eastern Ghats"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The Arabian Sea branch strikes the perpendicular wall of the Western Ghats (Sahyadris), forcing moisture-laden air to rise rapidly and dump heavy orographic rainfall along the Konkan coast."
    },
    {
        "q": "Based on the Walker Circulation diagram, why is an El Nino event typically associated with poor or deficit Indian monsoon rainfall?",
        "options": [
            "The equatorial warm water pool shifts eastward, weakening trade winds and disrupting the ascending branch of the Indian monsoon",
            "It permanently freezes all waters across the Indian Ocean",
            "It reverses Earth's axial spin from west-to-east to east-to-west",
            "It eliminates all atmospheric carbon dioxide"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "hard",
        "exp": "The diagram illustrates how El Nino displaces warm equatorial Pacific waters toward South America, weakening trade winds and suppressing convection over the Indian subcontinent."
    },
    {
        "q": "In Six's Maximum and Minimum Thermometer diagram, how are the indices positioned to record daily thermal extremes?",
        "options": [
            "Small steel dumbbell indices are pushed by the mercury meniscus and held in place by friction/magnets at the highest and lowest points",
            "The glass tube rotates 360 degrees when temperature shifts",
            "Air bubbles expand to shatter the glass capillary",
            "A digital laser measures the infrared beam automatically"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "In Six's thermometer, light magnetic steel indices are pushed ahead of the rising mercury columns. When the mercury retreats, friction holds the index at the peak extreme until reset with a magnet."
    },
    {
        "q": "Examining the diurnal curve of Relative Humidity versus Temperature, why does relative humidity reach its highest value at dawn?",
        "options": [
            "Air temperature reaches its daily minimum at dawn, minimizing saturation vapor pressure",
            "Atmospheric pressure drops to absolute zero at sunrise",
            "Solar radiation is most intense immediately before dawn",
            "Wind speed completely ceases worldwide every morning"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "As shown in the diurnal plot, radiative cooling lowers air temperature to its minimum near dawn. Because cooler air holds less water vapor, relative humidity peaks."
    },
    {
        "q": "Observing the synoptic weather map with isobar contours, in which direction will winds accelerate?",
        "options": [
            "From the High-pressure center (1024 hPa) toward the Low-pressure center (996 hPa)",
            "From Low pressure directly into High pressure",
            "In a stationary circle with zero movement",
            "Perpendicularly upward into outer space"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Air naturally moves down the pressure gradient from regions of high pressure toward regions of low pressure, modified by the Coriolis effect."
    },
    {
        "q": "According to the Numerical Weather Prediction (NWP) workflow diagram, what is the role of supercomputers like Pratyush and Mihir in Step 3?",
        "options": [
            "To solve mathematical equations governing atmospheric fluid dynamics and thermodynamics over global 3D grids",
            "To launch weather rockets into the mesosphere",
            "To broadcast radio audio directly to fishermen",
            "To manually paint cloud pictures for television news"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Step 3 highlights high-performance supercomputers integrating non-linear differential equations of fluid dynamics and thermodynamic state changes to project future weather states."
    },
    {
        "q": "Based on the IMD 4-Stage Color-Coded Alert System, what action is mandated when an area is placed under a RED alert?",
        "options": [
            "Take Action! Disaster management authorities and residents must initiate emergency measures",
            "No action needed, normal routine continues",
            "Simply check weather once next week",
            "Cancel all mobile phone networks"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The color scale specifies RED as 'Warning: Take Action', signaling severe weather capable of causing major disruption, loss of life, or property damage."
    },
    {
        "q": "Referring to the orographic precipitation diagram, why does the leeward side of the mountain experience a dry 'rain-shadow' climate?",
        "options": [
            "Descending air on the leeward slope warms adiabatically, decreasing relative humidity and preventing cloud formation/rainfall",
            "Clouds are physically too heavy to cross mountain peaks",
            "Mountains absorb all rainwater into their granite core",
            "The leeward slope has zero gravitational pull"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Air descending the leeward slope undergoes compressional warming. As it warms, its moisture-holding capacity increases, relative humidity plunges, and little or no rain falls (rain-shadow effect)."
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
