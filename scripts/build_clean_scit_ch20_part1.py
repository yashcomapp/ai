# scripts/build_clean_scit_ch20_part1.py
# Clean generator for MH-9-SCIT Chapter 20 Topic 20.1 (Subtopics 20.1.1, 20.1.2, 20.1.3, 20.1.4)
# 4 subtopics x 80 = 320 Qs
# Strictly compliant with Rule 2T: 40 Exam, 20 Practice, 20 Foundation per subtopic.

import json, sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_scit import build_q, generate_subtopic

CH_NUM = 20
CH_NAME = "Science General Knowledge & Discoveries"

def gen_20_1_1():
    tc = "MH-9-SCIT-20-20.1.1"
    tname = "Indian Space Research Organisation (ISRO) & Satish Dhawan Space Centre"
    archs = [
        # Arch 0: ISRO Founding, Vikram Sarabhai & Headquarters
        {
            'data': [
                ("the apex Indian national space agency founded on August 15, 1969, headquartered in Bengaluru, Karnataka", "Indian Space Research Organisation (ISRO)", "DRDO", "BARC", "TIFR"),
                ("the visionary scientist universally revered as the 'Father of the Indian Space Program'", "Dr. Vikram Sarabhai", "Dr. Homi J. Bhabha", "Dr. APJ Abdul Kalam", "Prof. Satish Dhawan"),
                ("the committee established by the Government of India in 1962 under the Department of Atomic Energy that preceded the formal founding of ISRO", "INCOSPAR (Indian National Committee for Space Research)", "Antrix Corporation", "NewSpace India Limited", "Space Applications Centre"),
                ("the southern coastal fishing village in Kerala where India's space journey began with the establishment of TERLS in 1963", "Thumba (Thumba Equatorial Rocket Launching Station, Thiruvananthapuram)", "Sriharikota", "Chandipur", "Mahendragiri"),
                ("the first sounding rocket successfully launched from Thumba on November 21, 1963, signaling India's entry into the space age", "Nike-Apache (procured from NASA)", "Rohini-75", "SLV-3", "Aryabhata"),
                ("the commercial arm of ISRO incorporated in 1992 to commercially market Indian space products and launch services worldwide", "Antrix Corporation Limited", "NewSpace India Limited (NSIL)", "IN-SPACe", "ISRO Telemetry Network"),
                ("the government body created in 2020 under the Department of Space to facilitate, authorize, and regulate private space sector activities in India", "IN-SPACe (Indian National Space Promotion and Authorization Centre)", "Antrix Corporation", "DRDO", "CSIR"),
                ("the primary Indian spaceport and rocket launch facility located on a barrier island in Tirupati district, Andhra Pradesh", "Satish Dhawan Space Centre (SDSC SHAR, Sriharikota)", "Thumba Equatorial Station", "Dr. Abdul Kalam Island", "Kulasekarapattinam"),
                ("the geographical feature of Sriharikota that makes it exceptionally advantageous for satellite rocket launches", "Located close to the Equator with eastward launch trajectory over the Bay of Bengal, utilizing Earth's rotational boost safely over open ocean", "Surrounded by mountains that block wind", "High desert altitude above 3000 m", "Zero atmospheric gravity"),
                ("the state-of-the-art propulsion complex of ISRO located at Mahendragiri in Tamil Nadu responsible for testing liquid and cryogenic rocket engines", "ISRO Propulsion Complex (IPRC, Mahendragiri)", "Space Applications Centre", "Liquid Propulsion Systems Centre", "Physical Research Laboratory")
            ],
            'tmpls': [
                "Which premier national space agency is defined as: {0}?",
                "Name the renowned visionary scientist recognized as: {0}.",
                "Which foundational committee is characterized as: {0}?",
                "Which historic coastal launching site represents: {0}?",
                "Identify the inaugural sounding rocket: {0}.",
                "Which public sector commercial enterprise corresponds to: {0}?",
                "Which regulatory national body is defined by: {0}?",
                "Which primary Indian launch site is identified as: {0}?",
                "What orbital mechanics and geographical rationale explains: {0}?",
                "Which rocket propulsion testing complex corresponds to: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Indian Space Program History**\\nThe prompt examines {item[0]}.\\n**Step 2: Institutional Framework and Geography**\\nISRO was envisioned by Dr. Vikram Sarabhai; Sriharikota provides equatorial velocity boost (\\(\\sim 460\\text{{ m/s}}\\)) and eastward oceanic safety corridors.\\n**Step 3: Verification**\\nThe matching institution is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 1: Launch Vehicles: SLV-3, ASLV, PSLV, GSLV & LVM3
        {
            'data': [
                ("India's first experimental satellite launch vehicle whose successful flight on July 18, 1980 placed the Rohini satellite (RS-1) into orbit", "SLV-3 (Satellite Launch Vehicle-3)", "ASLV", "PSLV", "GSLV"),
                ("the aerospace scientist who served as the Project Director for India's successful SLV-3 mission", "Dr. APJ Abdul Kalam", "Dr. Vikram Sarabhai", "Prof. UR Rao", "Dr. K. Sivan"),
                ("the four-stage launch vehicle universally acclaimed as the 'workhorse of ISRO' with over 50 successful missions deploying remote sensing satellites", "Polar Satellite Launch Vehicle (PSLV)", "Geosynchronous Satellite Launch Vehicle", "Sounding Rocket RH-200", "Small Satellite Launch Vehicle"),
                ("the fuel configuration used across the four stages of ISRO's Polar Satellite Launch Vehicle (PSLV)", "Solid (Stage 1) - Liquid (Stage 2, Vikas engine) - Solid (Stage 3) - Liquid (Stage 4)", "All four stages solid fuel", "All four stages liquid hydrogen", "Solid - Solid - Liquid - Cryogenic"),
                ("the launch vehicle capable of placing 2.5-tonne communication satellites into Geosynchronous Transfer Orbit (GTO) featuring an indigenous cryogenic upper stage", "GSLV Mk II", "PSLV-CA", "SLV-3", "ASLV"),
                ("India's heaviest operational three-stage launch vehicle colloquially nicknamed 'Bahubali' capable of launching 4 tonnes to GTO and 8 tonnes to LEO", "LVM3 (Launch Vehicle Mark 3 / GSLV Mk III)", "PSLV-XL", "GSLV Mk II", "SSLV"),
                ("the indigenous liquid rocket engine developed by Nambi Narayanan and ISRO teams used in PSLV Stage 2, GSLV Stage 2, and LVM3 core boosters", "Vikas engine (named after Vikram Ambalal Sarabhai)", "Cryogenic Engine CE-20", "Dhruva engine", "Kaveri jet engine"),
                ("the advanced high-thrust cryogenic rocket engine developed by ISRO for the upper stage (C25) of the LVM3 rocket, burning liquid hydrogen and liquid oxygen", "CE-20 cryogenic engine", "Vikas liquid engine", "CE-7.5 engine", "S200 solid booster"),
                ("the newly developed compact launch vehicle by ISRO designed for rapid, on-demand launch of mini and micro satellites up to 500 kg to low Earth orbit", "SSLV (Small Satellite Launch Vehicle)", "PSLV-XL", "GSLV Mk III", "Rohini-300"),
                ("the world record established by ISRO's PSLV-C37 mission on February 15, 2017", "Successfully deploying 104 satellites into orbit in a single mission", "First landing on Mars", "Fastest human spaceflight", "Deepest probe into Jupiter")
            ],
            'tmpls': [
                "Which historic indigenous launch vehicle is defined as: {0}?",
                "Name the renowned project director associated with: {0}.",
                "Which legendary launch vehicle is recognized as: {0}?",
                "What staged propellant sequence characterizes: {0}?",
                "Which geosynchronous launch vehicle corresponds to: {0}?",
                "Which heavy-lift launch vehicle represents: {0}?",
                "Which iconic liquid rocket engine corresponds to: {0}?",
                "Which high-thrust indigenous cryogenic engine represents: {0}?",
                "Which rapid-deployment launcher is defined as: {0}?",
                "What global astronautical milestone was achieved by: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Launch Vehicle Evolution Context**\\nThe statement details {item[0]}.\\n**Step 2: Staging and Rocket Engines**\\nFrom SLV-3 (solid) to PSLV (solid/liquid alternating) and LVM3 (S200 solid strap-ons, L110 Vikas core, C25 CE-20 cryogenic stage), ISRO advanced launch capabilities.\\n**Step 3: Verification**\\nThe matching launch vehicle or milestone is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 2: Satellites: Aryabhata, INSAT, IRS & NavIC
        {
            'data': [
                ("India's historic first satellite launched on April 19, 1975 using a Soviet Kosmos-3M launch vehicle, named after the ancient astronomer", "Aryabhata", "Bhaskara-I", "Rohini", "Apple"),
                ("India's first experimental geostationary communication satellite launched in 1981 carried on an Ariane rocket after antenna tests on an ox-cart", "APPLE (Ariane Passenger Payload Experiment)", "Aryabhata", "INSAT-1A", "EDUSAT"),
                ("the multipurpose geostationary satellite network established by ISRO for telecommunications, television broadcasting, and meteorological disaster warning", "INSAT (Indian National Satellite System) and GSAT series", "IRS series", "Cartosat series", "Oceansat series"),
                ("the premier earth observation satellite series of ISRO providing high-resolution multispectral imagery for agriculture, forestry, water mapping, and urban planning", "IRS (Indian Remote Sensing) / Cartosat / Resourcesat series", "INSAT series", "GSAT series", "AstroSat"),
                ("India's dedicated satellite launched in September 2004 exclusively for distance education and virtual classroom connectivity across rural India", "EDUSAT (GSAT-3)", "Aryabhata", "Cartosat-1", "HAMSAT"),
                ("India's independent regional satellite navigation system consisting of a constellation of 7 satellites providing precise real-time positioning across India", "NavIC (Navigation with Indian Constellation / IRNSS)", "GPS", "GLONASS", "Galileo"),
                ("the satellite-based air traffic navigation augmentation system jointly developed by ISRO and Airports Authority of India to guide civil aircraft landing", "GAGAN (GPS Aided GEO Augmented Navigation)", "NavIC", "Bhuvan", "AstroSat"),
                ("ISRO's indigenous web-based 3D geoportal offering high-resolution satellite imagery, topographic maps, and geospatial thematic analysis of India", "Bhuvan (bhuvan.nrsc.gov.in)", "Google Earth", "MapmyIndia", "BharatNet"),
                ("the dedicated multi-wavelength space astronomy observatory launched by ISRO in September 2015 studying celestial stars, black holes, and neutron stars", "AstroSat", "Cartosat-2", "RISAT-1", "HySIS"),
                ("the radar imaging satellite series of ISRO utilizing Synthetic Aperture Radar (SAR) capable of imaging Earth through clouds and night darkness", "RISAT / EOS-04 series", "INSAT-3DR", "Kalpana-1", "Megha-Tropiques")
            ],
            'tmpls': [
                "Which historic maiden Indian satellite is defined as: {0}?",
                "Which experimental communication satellite corresponds to: {0}?",
                "Which geostationary network represents: {0}?",
                "Which remote sensing satellite fleet is defined by: {0}?",
                "Which educational satellite milestone corresponds to: {0}?",
                "Which indigenous satellite navigation constellation represents: {0}?",
                "Which aviation navigation augmentation system corresponds to: {0}?",
                "Which indigenous geospatial 3D web platform represents: {0}?",
                "Which multi-wavelength astronomical observatory corresponds to: {0}?",
                "Which all-weather synthetic aperture radar satellite series represents: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Indian Satellite Constellations Context**\\nThe query highlights {item[0]}.\\n**Step 2: Applications and Specifications**\\nINSAT/GSAT serves telecommunication; IRS/Cartosat provides Earth observation; NavIC provides regional PNT (Positioning, Navigation, and Timing).\\n**Step 3: Verification**\\nThe correct satellite designation is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 3: Specialized Centres: VSSC, URSC, SAC & NRSC
        {
            'data': [
                ("the lead ISRO centre located in Thiruvananthapuram, Kerala responsible for design and development of launch vehicles (PSLV, GSLV, LVM3)", "Vikram Sarabhai Space Centre (VSSC)", "U R Rao Satellite Centre", "Space Applications Centre", "National Remote Sensing Centre"),
                ("the lead ISRO centre located in Bengaluru, Karnataka responsible for the design, development, assembly, and testing of all Indian satellites", "U R Rao Satellite Centre (URSC, formerly ISAC)", "Vikram Sarabhai Space Centre", "Liquid Propulsion Systems Centre", "Development and Educational Communication Unit"),
                ("the ISRO centre located in Ahmedabad, Gujarat that conceives and develops space-borne optical and microwave sensor payloads for communication and remote sensing", "Space Applications Centre (SAC)", "National Remote Sensing Centre", "Master Control Facility", "Physical Research Laboratory"),
                ("the ISRO centre located in Hyderabad, Telangana responsible for acquisition, processing, archiving, and dissemination of satellite remote sensing data", "National Remote Sensing Centre (NRSC, Shadnagar ground station)", "Space Applications Centre", "ISRO Telemetry Centre", "VSSC"),
                ("the primary ground station of ISRO located at Hassan in Karnataka and Bhopal in Madhya Pradesh that monitors and controls geostationary satellites in orbit", "Master Control Facility (MCF)", "ISTRAC", "VSSC", "IPRC"),
                ("the network of ground telemetry and tracking stations headquartered in Bengaluru with a deep space network at Byalalu to track interplanetary missions", "ISTRAC (ISRO Telemetry, Tracking and Command Network) & Indian Deep Space Network (IDSN)", "MCF Hassan", "SHAR Sriharikota", "VSSC Thiruvananthapuram"),
                ("the premier research institute in Ahmedabad founded in 1947 by Dr. Vikram Sarabhai conducting fundamental research in astronomy, planetary sciences, and geophysics", "Physical Research Laboratory (PRL, Ahmedabad)", "TIFR Mumbai", "Raman Research Institute", "IIA Bengaluru"),
                ("the autonomous academic institution established by the Department of Space in Thiruvananthapuram offering undergraduate and doctoral degrees in space science", "Indian Institute of Space Science and Technology (IIST)", "IIT Madras", "IISc Bengaluru", "NIT Calicut"),
                ("the massive 32-metre parabolic steerable deep space antenna installed at Byalalu near Bengaluru to communicate with Chandrayaan and Mangalyaan", "Indian Deep Space Network (IDSN-32)", "GMRT Pune", "Giant Metrewave Dish", "Ooty Radio Telescope"),
                ("the second launch port of ISRO currently being constructed in southern Tamil Nadu for dedicated commercial launches of Small Satellite Launch Vehicles (SSLV)", "Kulasekarapattinam (Thoothukudi district)", "Puri", "Kochi", "Visakhapatnam")
            ],
            'tmpls': [
                "Which primary launch vehicle development centre is defined as: {0}?",
                "Which premier satellite engineering centre corresponds to: {0}?",
                "Which sensor payload development centre represents: {0}?",
                "Which remote sensing data processing centre corresponds to: {0}?",
                "Which geostationary orbit control facility represents: {0}?",
                "Which deep space telemetry and tracking network is defined by: {0}?",
                "Which foundational space research institute corresponds to: {0}?",
                "Which specialized space science university represents: {0}?",
                "Which massive deep space tracking antenna is located at: {0}?",
                "Which upcoming southern commercial spaceport corresponds to: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Institutional ISRO Geography**\\nThe statement details {item[0]}.\\n**Step 2: Center Functions**\\nVSSC builds rockets, URSC builds satellites, SAC builds payloads, NRSC disseminates Earth imagery, and ISTRAC/IDSN tracks deep space missions.\\n**Step 3: Verification**\\nThe matching institution is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 4: Space Physics, Orbits & Orbital Velocity
        {
            'data': [
                ("the circular orbit around Earth at an altitude of approximately 35,786 km where a satellite's orbital period exactly equals Earth's rotation period (24 hours)", "Geostationary orbit (GEO, equatorial circular)", "Low Earth Orbit (LEO)", "Polar Sun-synchronous orbit", "Medium Earth Orbit"),
                ("the orbit passing over or near both polar regions of the Earth with an altitude of 600-800 km designed so that the satellite passes over any given point at the same local solar time", "Sun-synchronous Polar Orbit (SSO)", "Geostationary equatorial orbit", "Geosynchronous transfer orbit", "Molniya orbit"),
                ("an orbit situated relatively close to the Earth's surface between 200 km and 2,000 km, ideal for remote sensing, manned space stations, and spy satellites", "Low Earth Orbit (LEO)", "Geostationary Orbit", "High Earth Orbit", "Lagrange point orbit"),
                ("the minimum horizontal orbital velocity required for a satellite to maintain a stable circular orbit close to the Earth's surface (taking \\(g = 9.8\\text{ m/s}^2\\), \\(R = 6400\\text{ km}\\))", "Approximately \\(7.9\\text{ km/s } (\\approx 8\\text{ km/s} = 28,400\\text{ km/h})\\)", "\\(11.2\\text{ km/s}\\)", "\\(3.1\\text{ km/s}\\)", "\\(1.0\\text{ km/s}\\)"),
                ("the minimum speed required for an unpowered object to escape completely from Earth's gravitational field into interplanetary space", "Escape velocity (\\(v_e = \\sqrt{2gR} \\approx 11.2\\text{ km/s}\\))", "Orbital speed (\\(7.9\\text{ km/s}\\))", "Sound speed (\\(340\\text{ m/s}\\))", "Speed of light"),
                ("the mathematical relationship between orbital speed \\(v_o\\) in a low orbit and escape velocity \\(v_e\\) from Earth's surface", "\\(v_e = \\sqrt{2} \\times v_o \\approx 1.414 \\times v_o\\)", "\\(v_e = 2 \\times v_o\\)", "\\(v_e = \\frac{v_o}{\\sqrt{2}}\\)", "\\(v_e = v_o^2\\)"),
                ("the five gravitational equilibrium points in space where the combined gravitational forces of the Earth and Sun equal the centripetal force required to orbit with them", "Lagrange points (L1, L2, L3, L4, L5)", "Van Allen belts", "Keplerian apsides", "Roche limits"),
                ("why communication satellites are predominantly placed into geostationary orbits over the equator", "They appear permanently stationary in the sky relative to ground antennas, eliminating the need for steerable tracking dishes", "They are closer to stars", "They experience zero solar radiation", "They orbit faster than light"),
                ("the orbital mechanics technique of using the gravitational pull and orbital motion of a planet or moon to alter the path and speed of a spacecraft without expending fuel", "Gravitational slingshot (Gravity assist maneuver)", "Aerobraking", "Cryogenic staging", "Geostationary insertion"),
                ("the region of trapped charged subatomic particles (protons and electrons) held in place by Earth's magnetic field that satellites must navigate", "Van Allen radiation belts", "Ozone layer", "Troposphere", "Kuiper belt")
            ],
            'tmpls': [
                "Which 24-hour equatorial circular orbit is defined as: {0}?",
                "Which sun-synchronized orbital trajectory represents: {0}?",
                "Which low-altitude orbital band corresponds to: {0}?",
                "What is the theoretical low-Earth circular velocity for: {0}?",
                "What fundamental astronautical speed limit corresponds to: {0}?",
                "Which mathematical relation links: {0}?",
                "Which gravitational equilibrium points in space represent: {0}?",
                "What fixed celestial geometry rationale explains why: {0}?",
                "Which fuel-saving interplanetary flight dynamic represents: {0}?",
                "Which magnetospheric radiation zone is defined by: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Orbital Mechanics Context**\\nThe statement details {item[0]}.\\n**Step 2: Physics of Space Orbits**\\nOrbital speed \\(v_o = \\sqrt{{GM/R}} \\approx 7.9\\text{{ km/s}}\\); escape velocity \\(v_e = \\sqrt{{2GM/R}} = \\sqrt{{2}}v_o \\approx 11.2\\text{{ km/s}}\\). Geostationary altitude is \\(35,786\\text{{ km}}\\).\\n**Step 3: Verification**\\nThe matching physical concept is {item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 5: Sounding Rockets & Upper Atmosphere Research
        {
            'data': [
                ("one or two-stage solid propellant research rockets used for carrying scientific instrument packages into the upper atmosphere to take measurements", "Sounding rockets", "Intercontinental ballistic missiles", "Heavy-lift launchers", "Communication satellites"),
                ("the indigenous sounding rocket series developed by ISRO for upper atmospheric research and meteorological studies", "Rohini sounding rocket series (RH-75, RH-125, RH-200, RH-300, RH-560)", "Agni series", "Prithvi series", "BrahMos series"),
                ("the numerical number following 'RH' in Indian Rohini sounding rockets (e.g., RH-200, RH-560) represents", "The outer diameter of the rocket motor casing in millimetres", "The total payload mass in kilograms", "The maximum apogee altitude in kilometres", "The total fuel weight in tonnes"),
                ("the physical boundary altitude conventionally accepted by international aerospace federation (FAI) as the boundary between Earth's atmosphere and outer space", "Kármán line (altitude of 100 kilometres / 62 miles above sea level)", "Troposphere boundary (13 km)", "Stratopause (50 km)", "Geostationary altitude (35,786 km)"),
                ("the phenomenon in the equatorial upper atmosphere over Thumba (Kerala) characterized by a strong eastward narrow electric current at ~105 km altitude", "Equatorial Electrojet (EEJ)", "Aurora Borealis", "Polar vortex", "Van Allen belt"),
                ("why Thumba was chosen as India's first rocket launch site by Dr. Vikram Sarabhai and Dr. Homi Bhabha", "It lies directly on the magnetic equator of the Earth, making it ideal for in-situ sounding rocket investigations of the equatorial electrojet", "It had the lowest annual rainfall", "It was adjacent to the capital city", "It had active copper mines"),
                ("the solid propellant composition typically utilized in the motors of Indian Rohini sounding rockets", "Composite solid propellant based on Hydroxyl-Terminated Polybutadiene (HTPB) with ammonium perchlorate and aluminum powder", "Liquid kerosene and liquid oxygen", "Pure gasoline and alcohol", "Nitroglycerin only"),
                ("the space research experiment conducted by ISRO in 1975-76 using NASA's ATS-6 satellite to beam educational television programs to 2,400 Indian villages", "SITE (Satellite Instructional Television Experiment)", "EDUSAT project", "GramSat initiative", "Sarva Shiksha Abhiyan"),
                ("the small student-built sounding rocket payloads and nano-satellites promoted under ISRO's academic collaboration program", "POEM (PSLV Orbital Experimental Module) and Student Satellites (e.g., ANUSAT, Jugnu, Swayam)", "Gaganyaan module", "Aryabhata II", "INSAT-4A"),
                ("the specialized balloon-borne facility operated by TIFR and ISRO at Hyderabad for high-altitude cosmic ray and atmospheric studies", "National Balloon Facility (TIFR, Hyderabad)", "Hanle Observatory", "Physical Research Laboratory", "SHAR Sriharikota")
            ],
            'tmpls': [
                "Which atmospheric research vehicle class is defined as: {0}?",
                "Which indigenous suborbital rocket fleet represents: {0}?",
                "What physical rocket dimension is designated by: {0}?",
                "Which international aeronautical boundary represents: {0}?",
                "Which geomagnetic ionospheric current phenomenon represents: {0}?",
                "What geomagnetic rationale explains why: {0}?",
                "Which solid chemical propellant formulation is used in: {0}?",
                "Which historic mass rural educational broadcast project corresponds to: {0}?",
                "Which student experimental platform represents: {0}?",
                "Which specialized high-altitude balloon facility corresponds to: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Sounding Rocket and Atmospheric Research**\\nThe statement details {item[0]}.\\n**Step 2: Geomagnetic and Aerodynamic Science**\\nThumba lies on the magnetic equator ideal for studying the Equatorial Electrojet at ~105 km; Rohini numbers specify rocket caliber in mm.\\n**Step 3: Verification**\\nThe matching concept is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 6: Space Applications: Agriculture, Disaster Warning & Telemedicine
        {
            'data': [
                ("how ISRO's INSAT and GSAT weather satellites protect human lives along coastal India during severe Arabian Sea and Bay of Bengal cyclones", "By providing continuous high-frequency satellite infrared imaging and Doppler radar tracking to issue early storm surge and evacuation warnings", "By chemically suppressing the storm clouds", "By shooting laser beams at the cyclone", "By cooling ocean surface waters"),
                ("how ISRO's Cartosat and Resourcesat satellites assist Indian agriculture and crop yield estimation", "Through multispectral remote sensing monitoring Normalized Difference Vegetation Index (NDVI), soil moisture, crop acreage, and drought stress", "By directly spraying water from orbit", "By providing artificial sunlight at night", "By altering plant genes from space"),
                ("the application of space technology that connects specialist doctors in metropolitan hospitals with patients in remote rural healthcare centers via satellite", "Telemedicine network (ISRO Telemedicine program)", "Remote sensing", "Tele-education", "NavIC tracking"),
                ("the satellite technology used by the Indian National Centre for Ocean Information Services (INCOIS) to broadcast Potential Fishing Zone (PFZ) advisories to fishermen", "Ocean colour and sea surface temperature data from Oceansat satellites identifying nutrient-rich phytoplankton upwellings", "Sonar radar mapping", "Atmospheric air pressure sensors", "AstroSat deep space imagery"),
                ("the forest fire monitoring system developed by NRSC-ISRO that detects thermal anomalies across Indian forests within hours of occurrence", "Bhuvan-Forest Fire monitoring system (using MODIS and VIIRS satellite thermal sensors)", "INSAT radio beacons", "Airborne helicopter patrols", "Ground seismic sensors"),
                ("how satellite imagery aids post-disaster flood management in flood-prone states like Assam and Bihar", "Provides near-real-time flood inundation maps through cloud-penetrating synthetic aperture radar (SAR) to direct rescue and relief boats", "Drains floodwaters through space conduits", "Pumps water into aquifers directly", "Blocks monsoon clouds"),
                ("the tracking and communications technology installed on Indian Railways passenger and freight trains to provide real-time train movement information", "RTIS (Real-Time Train Information System) powered by ISRO's NavIC and Gagan transponders", "Cellular SMS towers only", "Track track-circuit bells", "Manual station telegraphs"),
                ("the satellite remote sensing technique used to detect underground mineral deposits, petroleum reservoirs, and groundwater aquifers", "Hyperspectral imaging and radiometric gamma survey", "Optical photography only", "Acoustic radar", "Thermal convection"),
                ("how space technology contributes to disaster search and rescue under the international COSPAS-SARSAT cooperative satellite system", "Distress alert beacons on aircraft, ships, and lifeboats transmit 406 MHz emergency signals detected by satellites to locate survivors globally", "Satellites dispatch rescue helicopters directly", "Satellites beam oxygen down to lifeboats", "Satellites pull lifeboats mechanically"),
                ("the specialized digital mapping system used by urban municipal corporations across India for property tax mapping, smart cities, and land records", "Geographic Information System (GIS) integrated with high-resolution Cartosat imagery", "Physical paper cadastral surveys", "Simple compass drafting", "Hand-drawn blueprints")
            ],
            'tmpls': [
                "What life-saving meteorological application describes: {0}?",
                "What agronomic remote sensing mechanism explains: {0}?",
                "Which public healthcare space initiative corresponds to: {0}?",
                "Which marine fishery advisory application is defined by: {0}?",
                "Which rapid environmental disaster alert system corresponds to: {0}?",
                "What emergency flood management technology explains how: {0}?",
                "Which railway tracking satellite technology corresponds to: {0}?",
                "Which geoscientific prospecting method represents: {0}?",
                "What international maritime search and rescue network explains: {0}?",
                "Which urban geospatial planning tool represents: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Socio-Economic Space Applications**\\nThe prompt examines {item[0]}.\\n**Step 2: Societal Integration of Space Tech**\\nRemote sensing and satellite communications provide direct societal benefits across agriculture, cyclone tracking, fishing advisories, and disaster relief.\\n**Step 3: Verification**\\nThe matching application is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 7: Quantitative Problems in Orbital Mechanics, Satellite Mass & Speed
        {
            'data': [
                ("A communication satellite orbits in a circular geostationary orbit of radius \\(r = 42,164\\text{ km}\\) from Earth's center. If it completes one orbit in \\(24\\text{ hours } (86,400\\text{ seconds})\\), calculate its orbital speed (\\(v = \\frac{2\\pi r}{T}\\)).", "\\(3.07\\text{ km/s } (\\approx 3.1\\text{ km/s})\\)", "\\(7.90\\text{ km/s}\\)", "\\(11.20\\text{ km/s}\\)", "\\(1.50\\text{ km/s}\\)"),
                ("A remote sensing satellite orbits in Low Earth Orbit at an altitude of \\(600\\text{ km}\\) above Earth's surface (orbital radius \\(R = 7000\\text{ km}\\)). If its orbital speed is \\(7.5\\text{ km/s}\\), calculate the time period of one revolution in minutes.", "\\(97.7\\text{ minutes } (\\approx 98\\text{ minutes})\\)", "\\(120.0\\text{ minutes}\\)", "\\(60.0\\text{ minutes}\\)", "\\(24.0\\text{ hours}\\)"),
                ("Calculate the theoretical escape velocity from the surface of the Moon taking lunar gravity \\(g_m = 1.62\\text{ m/s}^2\\) and lunar radius \\(R_m = 1737\\text{ km}\\) (\\(v_e = \\sqrt{2g_m R_m}\\)).", "\\(2.37\\text{ km/s } (\\approx 2.4\\text{ km/s})\\)", "\\(11.2\\text{ km/s}\\)", "\\(5.0\\text{ km/s}\\)", "\\(1.62\\text{ km/s}\\)"),
                ("The Polar Satellite Launch Vehicle (PSLV-C37) launched a total payload mass of \\(1378\\text{ kg}\\) into orbit comprising \\(104\\text{ satellites}\\). If Cartosat-2D weighed \\(714\\text{ kg}\\), calculate the combined mass of the remaining \\(103\\text{ co-passenger satellites}\\).", "\\(664\\text{ kg}\\)", "\\(714\\text{ kg}\\)", "\\(1378\\text{ kg}\\)", "\\(500\\text{ kg}\\)"),
                ("In a rocket launch, the rocket engine burns \\(200\\text{ kg}\\) of propellant per second and ejects exhaust gases at a velocity of \\(3000\\text{ m/s}\\). Calculate the thrust force generated (\\(F = \\frac{\\Delta m}{\\Delta t} \\times v_{\\text{exhaust}}\\)).", "\\(600,000\\text{ Newtons } (600\\text{ kN})\\)", "\\(150,000\\text{ N}\\)", "\\(200,000\\text{ N}\\)", "\\(1,200,000\\text{ N}\\)"),
                ("An LVM3 rocket has a total lift-off mass of \\(640\\text{ tonnes } (640,000\\text{ kg})\\). If the twin S200 solid rocket boosters produce a combined thrust of \\(10,000\\text{ kN } (10^7\\text{ N})\\), calculate the initial acceleration at lift-off (taking \\(g = 9.8\\text{ m/s}^2\\)).", "\\(5.825\\text{ m/s}^2\\)", "\\(15.625\\text{ m/s}^2\\)", "\\(9.800\\text{ m/s}^2\\)", "\\(2.500\\text{ m/s}^2\\)"),
                ("If a radio signal travels at the speed of light (\\(3 \\times 10^8\\text{ m/s}\\)), calculate the round-trip signal time delay (latency) to a geostationary satellite at an altitude of \\(36,000\\text{ km}\\).", "\\(0.24\\text{ seconds } (240\\text{ milliseconds})\\)", "\\(0.12\\text{ seconds}\\)", "\\(1.20\\text{ seconds}\\)", "\\(0.06\\text{ seconds}\\)"),
                ("A communication signal sent from Earth to a Mars rover at a distance of \\(2.25 \\times 10^8\\text{ km}\\) travels at \\(3 \\times 10^5\\text{ km/s}\\). How many minutes does the one-way signal take to reach Mars?", "\\(12.5\\text{ minutes } (750\\text{ seconds})\\)", "\\(8.3\\text{ minutes}\\)", "\\(25.0\\text{ minutes}\\)", "\\(5.0\\text{ minutes}\\)"),
                ("Calculate the gravitational force of attraction between a \\(1000\\text{ kg}\\) satellite in orbit and the Earth (mass \\(6 \\times 10^{24}\\text{ kg}\\)) at an orbital distance of \\(7000\\text{ km}\\) from Earth's center (taking \\(G = 6.67 \\times 10^{-11}\\text{ N}\\cdot\\text{m}^2/\\text{kg}^2\\)).", "\\(8167\\text{ Newtons } (\\approx 8.17\\text{ kN})\\)", "\\(9800\\text{ N}\\)", "\\(5000\\text{ N}\\)", "\\(6670\\text{ N}\\)"),
                ("A satellite in a circular orbit has an orbital kinetic energy of \\(50\\text{ Gigajoules (GJ)}\\). According to the virial theorem in celestial mechanics, what is the satellite's gravitational potential energy \\(U\\)?", "\\(-100\\text{ Gigajoules } (U = -2K)\\)", "\\(+100\\text{ GJ}\\)", "\\(-50\\text{ GJ}\\)", "\\(-25\\text{ GJ}\\)")
            ],
            'tmpls': [
                "Calculate geostationary satellite orbital velocity: {0}",
                "Compute low-Earth satellite orbital period: {0}",
                "Calculate lunar escape velocity: {0}",
                "Determine residual co-passenger payload mass: {0}",
                "Calculate rocket engine reaction thrust: {0}",
                "Compute rocket lift-off net acceleration: {0}",
                "Calculate satellite telecommunications signal latency: {0}",
                "Determine interplanetary radio transit time: {0}",
                "Compute orbital gravitational attraction force: {0}",
                "Evaluate orbital virial potential energy: {0}"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Formula and Given Quantities**\\nExtract orbital radius \\(r\\), velocity \\(v\\), thrust \\(F\\), or distance \\(d\\) from the problem.\\n**Step 2: Arithmetic Evaluation**\\nApply \\(v = \\frac{{2\\pi r}}{{T}}\\), \\(F = \\dot{{m}}v_{{e}}\\), \\(t = \\frac{{d}}{{c}}\\), or \\(F = G\\frac{{Mm}}{{r^2}}\\).\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)


def gen_20_1_2():
    tc = "MH-9-SCIT-20-20.1.2"
    tname = "Key missions: Chandrayaan lunar missions, Mangalyaan Mars Orbiter, Aditya-L1 solar observatory, Gaganyaan"
    archs = [
        # Arch 0: Chandrayaan-1 & Discovery of Water on the Moon
        {
            'data': [
                ("India's first lunar exploration mission launched on October 22, 2008 aboard PSLV-C11 that operated in lunar orbit for 312 days", "Chandrayaan-1", "Chandrayaan-2", "Chandrayaan-3", "Mangalyaan"),
                ("the groundbreaking scientific discovery made by Chandrayaan-1's Moon Mineralogy Mapper (M3, NASA payload) and Moon Impact Probe (MIP)", "Conclusive detection of water molecules (\\(H_2O\\)) and hydroxyl radicals (\\(OH\\)) on the lunar surface and polar regolith", "Discovery of lunar oil deposits", "Discovery of ancient plant fossils", "Discovery of lunar volcanic atmosphere"),
                ("the sub-probe released from Chandrayaan-1 on November 14, 2008 that impacted the lunar south pole near Shackleton crater carrying the Indian Tricolor", "Moon Impact Probe (MIP)", "Vikram lander", "Pragyan rover", "Smart-1"),
                ("the lunar impact site where the Moon Impact Probe (MIP) struck the Moon's south pole was officially named", "Jawahar Point (in honour of Jawaharlal Nehru)", "Shiv Shakti Point", "Tiranga Point", "Sarabhai Crater"),
                ("the prominent lunar impact crater in the Mare Serenitatis region named by the International Astronomical Union (IAU) after the founder of ISRO", "Sarabhai Crater", "Kalam Crater", "Bhabha Crater", "Raman Crater"),
                ("the chemical mapping payload built by ISRO on Chandrayaan-1 that mapped magnesium, aluminum, silicon, iron, and titanium across the Moon", "C1XS (Chandrayaan-1 X-ray Spectrometer)", "MIP", "Terrain Mapping Camera", "Sub-keV Atom Reflecting Analyzer"),
                ("the primary orbit of Chandrayaan-1 around the Moon used for global topographic and mineralogical mapping", "100 km circular polar orbit", "1000 km equatorial orbit", "Geostationary lunar orbit", "Moon-Sun L1 orbit"),
                ("the total number of scientific instruments (payloads) carried by Chandrayaan-1 including international payloads from NASA and ESA", "11 scientific instruments (5 Indian, 6 international)", "4 instruments", "20 instruments", "2 instruments"),
                ("the Terrain Mapping Camera (TMC) on Chandrayaan-1 produced what unique cartographic achievement of the Moon", "High-resolution 3D digital elevation model (DEM) of the entire lunar surface", "Color video of lunar sunrise", "Underground radar map of core", "Atmospheric cloud map"),
                ("how the Chandrayaan-1 mission ended in August 2009 after exceeding its planned primary mission objectives", "Radio communication with the orbiter was lost on August 29, 2009 due to thermal sensor failure", "It crashed into the Sun", "It returned to Earth with rock samples", "It was caught by Mars gravity")
            ],
            'tmpls': [
                "Which landmark maiden lunar mission is defined as: {0}?",
                "Which monumental lunar scientific discovery was achieved by: {0}?",
                "Which lunar impact sub-probe corresponds to: {0}?",
                "Name the designated lunar geographical impact site: {0}.",
                "Which prominent lunar crater is commemorated as: {0}?",
                "Which X-ray mineralogical payload represents: {0}?",
                "What operational orbital altitude was maintained by: {0}?",
                "What payload instrumentation suite characterized: {0}?",
                "Which cartographic digital modeling achievement was delivered by: {0}?",
                "What mission conclusion event occurred during: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Chandrayaan-1 Mission Context**\\nThe statement details {item[0]}.\\n**Step 2: Lunar Science Discoveries**\\nChandrayaan-1 discovered widespread hydroxyl (\\(OH\\)) and water (\\(H_2O\\)) signatures across the lunar surface via M3 and MIP.\\n**Step 3: Verification**\\nThe matching mission entity is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 1: Chandrayaan-2: Orbiter, Vikram Lander & Pragyan Rover
        {
            'data': [
                ("India's second lunar mission launched on July 22, 2019 aboard GSLV Mk III-M1 comprising an Orbiter, Vikram Lander, and Pragyan Rover", "Chandrayaan-2", "Chandrayaan-1", "Chandrayaan-3", "Artemis-1"),
                ("the naming of Chandrayaan-2's lunar lander in honor of the father of the Indian space program", "Vikram (named after Dr. Vikram Sarabhai)", "Pragyan", "Kalam", "Dhawan"),
                ("the naming of Chandrayaan-2 and 3's six-wheeled lunar robotic rover, derived from the Sanskrit word for 'wisdom'", "Pragyan", "Vikram", "Pushpak", "Vyommitra"),
                ("the high-resolution optical camera on the Chandrayaan-2 Orbiter that provides the sharpest lunar imagery from orbit with 25 cm spatial resolution", "Orbiter High Resolution Camera (OHRC)", "Terrain Mapping Camera", "CLASS", "IIRS"),
                ("the planned landing location on the Moon targeted by Chandrayaan-2 that had never been explored by any country before", "High-latitude lunar South Polar region (~70° South latitude)", "Lunar North Pole", "Sea of Tranquility on equator", "Far side of the Moon"),
                ("the technical failure that occurred during the final powered descent phase of the Vikram lander on September 7, 2019 at 2.1 km altitude", "Software guidance glitch and velocity accumulation caused a hard impact landing on the lunar surface", "The parachute failed to open", "The rocket ran out of fuel completely", "The lander was struck by a meteorite"),
                ("the operational status and scientific contribution of the Chandrayaan-2 Orbiter following the lander's hard landing", "The Orbiter continues to operate flawlessly in a 100 km lunar polar orbit, sending invaluable high-resolution science data for over 7 years", "The Orbiter was lost immediately", "The Orbiter returned to Earth", "The Orbiter crashed into the Moon"),
                ("the scientific payload on the Chandrayaan-2 Orbiter that detected the presence of Argon-40 in the tenuous lunar exosphere", "CHACE-2 (Chandra's Atmospheric Composition Explorer-2)", "CLASS", "OHRC", "DFSAR"),
                ("the Dual Frequency Synthetic Aperture Radar (DFSAR) on Chandrayaan-2 proved critical for", "Subsurface lunar imaging and mapping permanently shadowed water ice deposits in deep polar craters", "Communicating with Earth without antennas", "Measuring solar wind magnetism", "Photographing landing flags"),
                ("the lessons and engineering upgrades learned from Chandrayaan-2 that guaranteed the total success of Chandrayaan-3", "Reinforced landing legs, expanded landing footprint (4 km x 2.4 km), hazard detection sensors, software agility, and more fuel", "Replacing rockets with balloons", "Landing only in daytime on the equator", "Abandoning rovers entirely")
            ],
            'tmpls': [
                "Which composite lunar exploratory mission is defined as: {0}?",
                "Name the lunar robotic lander designated as: {0}.",
                "Which six-wheeled robotic rover corresponds to: {0}?",
                "Which high-resolution orbiter imaging payload represents: {0}?",
                "Which unprecedented lunar target destination was selected for: {0}?",
                "What engineering anomaly occurred during: {0}?",
                "What ongoing scientific operational role characterizes: {0}?",
                "Which exospheric spectrometer payload corresponds to: {0}?",
                "Which dual-frequency radar capability represents: {0}?",
                "What redesign engineering philosophy ensured: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Chandrayaan-2 Mission Context**\\nThe prompt examines {item[0]}.\\n**Step 2: Technical Architecture and Outcomes**\\nChandrayaan-2 comprised Orbiter, Vikram, and Pragyan; while the lander hard-landed, the Orbiter remains one of the premier lunar science platforms in history.\\n**Step 3: Verification**\\nThe matching concept is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 2: Chandrayaan-3: Historic South Pole Landing & National Space Day
        {
            'data': [
                ("India's third lunar exploration mission launched on July 14, 2023 aboard LVM3-M4 that achieved a historic soft landing on the Moon on August 23, 2023", "Chandrayaan-3", "Chandrayaan-2", "Luna-25", "Artemis-2"),
                ("the historic geopolitical and scientific milestone achieved by India with the Chandrayaan-3 landing", "India became the first country in human history to land near the lunar South Pole, and the fourth country to soft-land on the Moon", "First country to orbit the Moon", "First country to bring Moon soil", "First country to send humans to Moon"),
                ("the official name bestowed by Prime Minister Narendra Modi on the Chandrayaan-3 landing site near the lunar South Pole (69.37° S, 32.35° E)", "Shiv Shakti Point", "Tiranga Point", "Jawahar Point", "Sarabhai Point"),
                ("the official name bestowed on the impact point where the Chandrayaan-2 Vikram lander crash-landed on the Moon in 2019", "Tiranga Point", "Shiv Shakti Point", "Jawahar Point", "Ashoka Point"),
                ("the national commemorative day declared by the Government of India to be celebrated annually on August 23 to honor Chandrayaan-3's historic landing", "National Space Day (Rashtriya Antariksh Divas)", "National Science Day", "National Technology Day", "Engineers Day"),
                ("the scientific instrument on the Pragyan rover (LIBS) that made the first in-situ confirmation of which element on the lunar south pole surface", "Sulphur (\\(S\\)) unambiguously detected along with Al, Ca, Fe, Cr, Ti, Mn, Si, and O", "Liquid mercury", "Gaseous chlorine", "Uranium-235"),
                ("the payload on Vikram lander (ChaSTE) that measured the first-ever thermal conductivity and vertical temperature gradient of the lunar topsoil", "ChaSTE (Chandra's Surface Thermophysical Experiment)", "RAMBHA-LP", "ILSA", "LIBS"),
                ("the unexpected finding of ChaSTE showing the extreme thermal insulation property of lunar regolith near the South Pole", "Surface temperature was ~50°C, but plunged drastically to -10°C just 8 cm below the surface (a 60°C difference in 8 cm)", "Temperature was uniform throughout", "The soil was red hot at 500°C", "Soil was completely melted"),
                ("the payload on Vikram lander (ILSA) that recorded the first in-situ lunar seismic activity and vibrations of the rover roaming the surface", "ILSA (Instrument for Lunar Seismic Activity)", "ChaSTE", "APXS", "SHAPE"),
                ("the successful hop experiment executed by the Vikram lander on the Moon on September 3, 2023 demonstrated", "Lander fired engines, elevated 40 cm, moved laterally 30 cm, and landed safely, proving capability for future sample-return and human missions", "The lander flew back into Earth orbit", "The lander burrowed deep underground", "The lander rotated like a windmill")
            ],
            'tmpls': [
                "Which triumphant lunar exploration mission is defined as: {0}?",
                "What global astronautical supremacy milestone describes: {0}?",
                "Identify the official lunar landing geographical name: {0}.",
                "Identify the commemorated 2019 lunar point: {0}.",
                "Which national scientific annual celebration corresponds to: {0}?",
                "Which elemental discovery was spectroscopically confirmed by: {0}?",
                "Which thermal probe experiment corresponds to: {0}?",
                "What remarkable temperature gradient finding was revealed by: {0}?",
                "Which lunar seismometer instrument corresponds to: {0}?",
                "What future sample-return engineering capability was proven by: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Chandrayaan-3 Historic Mission Context**\\nThe statement details {item[0]}.\\n**Step 2: South Pole Discoveries**\\nLanded Aug 23, 2023 at Shiv Shakti Point; LIBS discovered Sulphur; ChaSTE measured 60°C gradient over 8 cm; hop experiment demonstrated lunar ascent capability.\\n**Step 3: Verification**\\nThe matching entity is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 3: Mangalyaan (Mars Orbiter Mission - MOM)
        {
            'data': [
                ("India's first interplanetary mission launched on November 5, 2013 aboard PSLV-C25 that entered Mars orbit on September 24, 2014", "Mars Orbiter Mission (MOM / Mangalyaan)", "Chandrayaan-1", "Aditya-L1", "ExoMars"),
                ("the historic world records established by ISRO with the Mangalyaan mission", "India became the first Asian nation to reach Mars orbit, and the first nation in the world to successfully reach Mars on its very maiden attempt", "First nation to land humans on Mars", "First nation to discover life on Mars", "First country to orbit Venus"),
                ("the remarkably frugal budget of the Mangalyaan mission (approximately ₹450 crore / $74 million), famously noted as being cheaper than", "The Hollywood science fiction movie 'Gravity' ($100 million) and less than auto-rickshaw fare per kilometre (~₹7/km)", "Building a single railway station", "A commercial passenger plane", "A smartphone manufacturing plant"),
                ("the color camera on Mangalyaan that captured spectacular global full-disc images of Mars, the Olympus Mons volcano, and its moon Phobos", "Mars Colour Camera (MCC)", "Thermal Infrared Imaging Spectrometer", "Lyman Alpha Photometer", "MENCA"),
                ("the orbital insertion burn (Mars Orbit Insertion - MOI) where Mangalyaan fired its 440 N Liquid Apogee Motor (LAM) on September 24, 2014 after", "Remaining dormant in deep space for nearly 300 days during interplanetary cruise", "Refueling at a space station", "Being serviced by astronauts", "Being recharged on Moon"),
                ("the planned design mission life of Mangalyaan versus its actual operational lifespan in Mars orbit", "Designed for 6 months; operated successfully for over 7.5 years (until April 2022)", "Designed for 10 years; lasted 1 month", "Designed for 1 week; lasted 1 year", "Designed for 2 years; lasted 2 years"),
                ("the exospheric neutral composition analyzer (MENCA) on Mangalyaan studied", "The composition and density of the upper Martian atmosphere during dust storms", "Martian seismic waves", "Water canals on Mars surface", "Martian core gravity"),
                ("the interplanetary trajectory method used by ISRO to propel Mangalyaan from Earth to Mars using minimum rocket fuel", "Hohmann transfer orbit following multiple Earth-bound elliptical orbit-raising maneuvers", "Direct linear propulsion", "Laser beam acceleration", "Nuclear thermal rocket"),
                ("the natural optical phenomenon captured by Mangalyaan's Mars Colour Camera showing the far side of Mars' moon Phobos against the backdrop of Mars", "Phobos transit across the Martian surface", "Solar eclipse on Jupiter", "Earthrise from Mars", "Comet collision"),
                ("the team of aerospace scientists celebrated as the 'Rocket Women of India' who played key leadership roles in Mangalyaan", "Ritu Karidhal (Mission Director), Nandini Harinath, Anuradha TK, and Moumita Dutta", "Kalpana Chawla and Sunita Williams", "Marie Curie and Rosalind Franklin", "Janaki Ammal and Asima Chatterjee")
            ],
            'tmpls': [
                "Which historic interplanetary maiden mission is defined as: {0}?",
                "What unprecedented global astronautical record was achieved by: {0}?",
                "What famous financial frugality benchmark illustrates: {0}?",
                "Which optical imaging instrument corresponds to: {0}?",
                "What deep space propulsion restart milestone characterized: {0}?",
                "What extraordinary mission lifespan longevity characterized: {0}?",
                "Which Martian atmospheric science payload represents: {0}?",
                "Which fuel-efficient orbital trajectory transfer describes: {0}?",
                "Which planetary satellite imaging milestone was captured by: {0}?",
                "Which pioneering female aerospace leaders are celebrated as: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Mangalyaan Mission Context**\\nThe query examines {item[0]}.\\n**Step 2: Interplanetary Mechanics and Records**\\nLaunched Nov 2013, entered Mars orbit Sept 2014; first nation successful on maiden attempt; operated for 7.5 years via Hohmann transfer orbit.\\n**Step 3: Verification**\\nThe correct space mission answer is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 4: Aditya-L1 Solar Observatory & Lagrange Points
        {
            'data': [
                ("India's first dedicated space-based solar observatory mission launched on September 2, 2023 aboard PSLV-C57", "Aditya-L1", "AstroSat", "Chandrayaan-3", "XPoSat"),
                ("the specific celestial destination in space where Aditya-L1 was successfully placed on January 6, 2024", "A halo orbit around the Sun-Earth Lagrange point 1 (L1), located approximately 1.5 million km from Earth", "A low Earth orbit at 400 km", "Geostationary orbit at 36,000 km", "Lunar polar orbit"),
                ("the major scientific advantage of placing a solar observatory in a halo orbit around the Sun-Earth L1 point", "Provides continuous, uninterrupted view of the Sun without any occultation, eclipses, or Earth atmospheric interference", "It is closer to the Moon", "It experiences zero solar heat", "It orbits inside Earth's magnetic core"),
                ("the primary optical payload on Aditya-L1 designed to observe the solar corona and coronal mass ejections (CMEs) in visible and ultraviolet light", "VELC (Visible Emission Line Coronagraph)", "SUIT", "ASPEX", "PAPA"),
                ("the ultraviolet telescope on Aditya-L1 (SUIT) designed to image the full solar disc in the near-ultraviolet wavelength band (200-400 nm)", "SUIT (Solar Ultraviolet Imaging Telescope)", "VELC", "SoLEXS", "HEL1OS"),
                ("the explosive ejection of billions of tonnes of magnetized plasma from the Sun's corona into interplanetary space that can disrupt power grids and satellites on Earth", "Coronal Mass Ejection (CME)", "Solar eclipse", "Sunspot minimum", "Solar wind calm"),
                ("the solar wind particle analyzer on Aditya-L1 designed to measure the composition and energy of solar wind protons and alpha particles in-situ", "ASPEX (Aditya Solar wind Particle Experiment) and PAPA", "VELC", "SUIT", "MAG"),
                ("the outermost, extremely hot layer of the Sun's atmosphere extending millions of kilometres into space whose heating mechanism Aditya-L1 investigates", "Solar Corona (temperatures exceed 1 to 2 million Kelvin, paradoxically far hotter than the 6,000 K solar surface)", "Photosphere", "Chromosphere", "Solar core"),
                ("the payload on Aditya-L1 that measures interplanetary magnetic fields at the L1 point to detect approaching solar storm fronts", "MAG (Digital Magnetometer)", "SUIT", "VELC", "HEL1OS"),
                ("the high-energy X-ray spectrometer on Aditya-L1 that monitors hard X-ray emissions during dynamic solar flare eruptions", "HEL1OS (High Energy L1 Orbiting X-ray Spectrometer)", "VELC", "PAPA", "ASPEX")
            ],
            'tmpls': [
                "Which dedicated solar astrophysical mission is defined as: {0}?",
                "Which celestial orbital destination represents: {0}?",
                "What uninterrupted viewing advantage explains why: {0}?",
                "Which flagship coronal imaging payload corresponds to: {0}?",
                "Which full-disc ultraviolet imaging telescope represents: {0}?",
                "Which violent solar space weather eruption is defined as: {0}?",
                "Which in-situ solar wind particle analyzer corresponds to: {0}?",
                "Which enigmatic ultra-hot solar atmospheric layer represents: {0}?",
                "Which magnetic field sensor payload corresponds to: {0}?",
                "Which hard X-ray solar flare spectrometer represents: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Aditya-L1 Science Context**\\nThe statement details {item[0]}.\\n**Step 2: Solar Physics at Lagrange Point 1**\\nLocated at L1 (1.5 million km Sun-ward); VELC and SUIT observe the solar corona and CMEs to understand the coronal heating paradox and space weather.\\n**Step 3: Verification**\\nThe matching mission entity is {item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 5: Gaganyaan: India's Human Spaceflight Programme
        {
            'data': [
                ("India's prestigious national human spaceflight program aiming to demonstrate indigenous capability to launch a human crew of 3 to Low Earth Orbit (400 km)", "Gaganyaan", "Chandrayaan", "Mangalyaan", "Shukrayaan"),
                ("the heavy-lift rocket human-rated by ISRO to launch the Gaganyaan crew module into space safely", "Human-Rated LVM3 (HLVM3)", "PSLV-XL", "GSLV Mk II", "SSLV"),
                ("the female-looking half-humanoid robot developed by ISRO to fly aboard uncrewed Gaganyaan test flights to test life support and cabin parameters", "Vyommitra (derived from Sanskrit 'Vyoma' meaning space and 'Mitra' meaning friend)", "Pragyan", "Vikram", "Pushpak"),
                ("the four Indian Air Force test pilots selected and introduced to the nation in February 2024 as astronaut-designates for the Gaganyaan mission", "Group Captains Prashanth Balakrishnan Nair, Ajit Krishnan, Angad Prathap, and Wing Commander Shubhanshu Shukla", "Rakesh Sharma, Ravish Malhotra, Kalpana Chawla, and Sunita Williams", "Vikram Sarabhai, APJ Abdul Kalam, Satish Dhawan, and UR Rao", "Abhinandan Varthaman, BS Dhanoa, Arjan Singh, and Subroto Mukerjee"),
                ("the critical safety mechanism tested in the TV-D1 mission (October 2023) designed to pull the crew module away rapidly in case of rocket launch abort", "Crew Escape System (CES)", "Parachute reefing", "Orbital module thruster", "Heat shield ejector"),
                ("the orbital altitude and mission duration planned for the inaugural crewed Gaganyaan flight", "Low Earth Orbit at ~400 km altitude for a 3-day mission, followed by splashdown in the Arabian Sea / Bay of Bengal", "100 km orbit for 1 hour", "Geostationary orbit for 1 month", "Lunar orbit for 2 weeks"),
                ("the astronaut training facility established by the Indian Air Force and ISRO in Bengaluru for psychological, centrifuge, and physical training", "Astronaut Training Facility (Institute of Aerospace Medicine - IAM, Bengaluru)", "VSSC Thiruvananthapuram", "National Defence Academy Pune", "Air Force Academy Dundigal"),
                ("the special environmental control and life support system (ECLSS) inside the Gaganyaan crew module must maintain", "Breathable atmospheric pressure, oxygen (\\(O_2\\)) supply, carbon dioxide (\\(CO_2\\)) scrubbing, and temperature/humidity control", "Zero air pressure", "100% pure carbon dioxide", "Liquid nitrogen immersion"),
                ("the heat shield material on the bottom of the Gaganyaan crew module protects the astronauts from what extreme temperature during atmospheric re-entry", "Thermal temperatures exceeding 2,000°C to 3,000°C caused by intense atmospheric compression and friction", "Sub-zero temperatures of -200°C", "Solar ultraviolet rays only", "Cosmic gamma rays"),
                ("the primary maritime agency collaborating with ISRO to conduct rapid recovery operations of the crew module after sea splashdown", "Indian Navy", "Indian Coast Guard alone", "Border Security Force", "Port Trust of India")
            ],
            'tmpls': [
                "Which human spaceflight programme is defined as: {0}?",
                "Which human-rated launch vehicle is designated for: {0}?",
                "Name the spacefaring humanoid robot: {0}.",
                "Which decorated astronaut-designates were selected for: {0}?",
                "Which emergency abort safety architecture was validated in: {0}?",
                "What planned flight profile characterizes: {0}?",
                "Which specialized astronaut training centre represents: {0}?",
                "What environmental life-support parameters are mandated by: {0}?",
                "What thermal re-entry protection is engineered for: {0}?",
                "Which armed service leads the maritime recovery operations for: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Gaganyaan Program Context**\\nThe statement details {item[0]}.\\n**Step 2: Human Spaceflight Engineering**\\nHLVM3 launches 3 astronauts to 400 km for 3 days; Vyommitra tests uncrewed flights; CES ensures launchpad/in-flight abort safety.\\n**Step 3: Verification**\\nThe matching entity is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 6: Future Planetary Frontiers: Shukrayaan, LUPEX, Bharatiya Antariksh Station
        {
            'data': [
                ("India's proposed planetary orbiter mission to study the dense, acidic atmosphere and volcanic surface of planet Venus", "Shukrayaan (Venus Orbiter Mission)", "Mangalyaan-2", "Aditya-L2", "Chandrayaan-4"),
                ("the joint lunar polar exploration mission planned between ISRO (India) and JAXA (Japan) to land a heavy rover near the Moon's South Pole", "LUPEX (Lunar Polar Exploration Mission / Chandrayaan-5)", "Artemis-3", "Mars Sample Return", "BepiColombo"),
                ("the visionary national space station planned by India to be assembled in Low Earth Orbit by 2035 announced by the Prime Minister", "Bharatiya Antariksh Station (BAS)", "International Space Station", "Tiangong", "Mir"),
                ("India's planned lunar sample return mission (Chandrayaan-4) designed to collect lunar soil and return it safely to Earth", "Chandrayaan-4 (Lunar Sample Return Mission)", "Chandrayaan-3", "Gaganyaan-2", "AstroSat-2"),
                ("the national astronautical target set by India for landing an Indian astronaut on the surface of the Moon", "By the year 2040", "By 2025", "By 2030", "By 2050"),
                ("the autonomous winged aerospace vehicle developed by ISRO that took off, flew, and landed autonomously on a runway in Karnataka in 2023-24", "RLV-LEX (Reusable Launch Vehicle Autonomous Landing Experiment 'Pushpak')", "Tejas LCA", "Gaganyaan", "Saras"),
                ("the space docking experiment planned by ISRO to demonstrate autonomous docking of two spacecraft in orbit, vital for space station assembly", "SPADEX (Space Docking Experiment)", "POEM", "XPoSat", "RISAT"),
                ("the dedicated satellite mission launched by ISRO on January 1, 2024 to study the polarization of cosmic X-rays from black holes and neutron stars", "XPoSat (X-ray Polarimeter Satellite)", "AstroSat", "Aditya-L1", "Cartosat-3"),
                ("the air-breathing rocket engine technology successfully tested by ISRO that scoops atmospheric oxygen during supersonic flight to burn fuel", "Scramjet (Supersonic Combustion Ramjet) engine", "Cryogenic CE-20", "Vikas liquid engine", "Solid rocket booster"),
                ("the commercial Earth-observation satellite joint mission being developed by NASA and ISRO carrying dual-frequency L-band and S-band radar", "NISAR (NASA-ISRO Synthetic Aperture Radar)", "Cartosat-4", "Oceansat-3", "INSAT-3DS")
            ],
            'tmpls': [
                "Which upcoming planetary mission to Venus corresponds to: {0}?",
                "Which Indo-Japanese lunar partnership mission is defined by: {0}?",
                "Which future orbital space station vision represents: {0}?",
                "Which upcoming lunar soil return initiative corresponds to: {0}?",
                "What official national astronautical target timeline governs: {0}?",
                "Which autonomous winged reusable space plane represents: {0}?",
                "Which autonomous in-orbit rendezvous mission corresponds to: {0}?",
                "Which cosmic X-ray polarization satellite launched in 2024 represents: {0}?",
                "Which hypersonic air-breathing propulsion technology corresponds to: {0}?",
                "Which flagship dual-radar NASA-ISRO partnership represents: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Future Space Frontiers Context**\\nThe prompt examines {item[0]}.\\n**Step 2: Indian Space Vision 2040**\\nRoadmap includes Bharatiya Antariksh Station (2035), lunar landing (2040), Chandrayaan-4 sample return, Shukrayaan Venus orbiter, and NISAR radar.\\n**Step 3: Verification**\\nThe matching mission entity is {item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 7: Quantitative Problems in Lunar/Mars Trajectories & Mission Metrics
        {
            'data': [
                ("The mass of Chandrayaan-3 at launch was \\(3900\\text{ kg}\\), consisting of the Propulsion Module (\\(2148\\text{ kg}\\)) and the Lander Module (Vikram + Pragyan). Calculate the mass of the Lander Module.", "\\(1752\\text{ kg } (3900 - 2148 = 1752\\text{ kg})\\)", "\\(1500\\text{ kg}\\)", "\\(2000\\text{ kg}\\)", "\\(1250\\text{ kg}\\)"),
                ("The Pragyan rover deployed from Vikram has a mass of \\(26\\text{ kg}\\) and carries solar panels generating \\(50\\text{ Watts}\\) of power. If Vikram's lander mass is \\(1752\\text{ kg}\\), what is the dry mass of Vikram alone without Pragyan?", "\\(1726\\text{ kg } (1752 - 26 = 1726\\text{ kg})\\)", "\\(1700\\text{ kg}\\)", "\\(1650\\text{ kg}\\)", "\\(1750\\text{ kg}\\)"),
                ("A lunar day equals \\(14\\text{ Earth days}\\) of continuous sunlight, followed by \\(14\\text{ Earth days}\\) of freezing lunar night. How many hours of sunlight did Chandrayaan-3 have during its primary operational mission?", "\\(336\\text{ hours } (14 \\times 24 = 336\\text{ hours})\\)", "\\(168\\text{ hours}\\)", "\\(720\\text{ hours}\\)", "\\(240\\text{ hours}\\)"),
                ("The distance between Earth and Sun at the L1 Lagrange point where Aditya-L1 operates is \\(1.5 \\times 10^6\\text{ km}\\). If total Earth-Sun distance is \\(1.5 \\times 10^8\\text{ km}\\), what percentage of the distance to the Sun did Aditya-L1 travel?", "\\(1.0\\%\\)", "\\(10.0\\%\\)", "\\(0.1\\%\\)", "\\(5.0\\%\\)"),
                ("Light travels at \\(300,000\\text{ km/s}\\). Calculate the time taken for sunlight to travel from the Sun to Aditya-L1 at the L1 point (distance \\(1.485 \\times 10^8\\text{ km}\\)).", "\\(495\\text{ seconds } (8.25\\text{ minutes})\\)", "\\(500\\text{ seconds}\\)", "\\(100\\text{ seconds}\\)", "\\(1000\\text{ seconds}\\)"),
                ("During the Chandrayaan-3 landing descent, Vikram decelerated from an orbital velocity of \\(1680\\text{ m/s}\\) to \\(0\\text{ m/s}\\) in \\(1150\\text{ seconds}\\). Calculate the average deceleration rate.", "\\(1.46\\text{ m/s}^2\\)", "\\(9.80\\text{ m/s}^2\\)", "\\(0.50\\text{ m/s}^2\\)", "\\(3.20\\text{ m/s}^2\\)"),
                ("The Pragyan rover traveled a total cumulative distance of over \\(100\\text{ metres}\\) across the lunar surface during its 10 days of roving. If it moved at an average speed of \\(1\\text{ cm/s } (0.01\\text{ m/s})\\), calculate total roving time in hours.", "\\(2.78\\text{ hours } (10,000\\text{ seconds})\\)", "\\(10.0\\text{ hours}\\)", "\\(1.0\\text{ hour}\\)", "\\(24.0\\text{ hours}\\)"),
                ("The cost of Mangalyaan was ₹450 crore (₹4.5 billion). If the total distance covered along its interplanetary trajectory was \\(680 \\times 10^6\\text{ km}\\), calculate the cost per kilometre traveled.", "\\(\\approx ₹6.62\\text{ per kilometre}\\)", "\\(₹66.2\\text{ per km}\\)", "\\(₹0.66\\text{ per km}\\)", "\\(₹662\\text{ per km}\\)"),
                ("The Gaganyaan crew module will orbit at \\(400\\text{ km}\\) altitude with an orbital speed of \\(7.67\\text{ km/s}\\). If Earth's radius is \\(6400\\text{ km}\\) (orbit circumference \\(2\\pi \\times 6800\\text{ km} \\approx 42,725\\text{ km}\\)), calculate orbital period in minutes.", "\\(92.8\\text{ minutes } (\\approx 93\\text{ minutes})\\)", "\\(60.0\\text{ minutes}\\)", "\\(120.0\\text{ minutes}\\)", "\\(45.0\\text{ minutes}\\)"),
                ("An astronaut of mass \\(75\\text{ kg}\\) weighs \\(735\\text{ N}\\) on Earth. Taking lunar surface gravity as \\(g_m = 1.62\\text{ m/s}^2\\), calculate the astronaut's weight on the lunar surface.", "\\(121.5\\text{ Newtons } (\\approx \\frac{1}{6}\\text{th of Earth weight})\\)", "\\(735\\text{ N}\\)", "\\(75\\text{ N}\\)", "\\(243\\text{ N}\\)")
            ],
            'tmpls': [
                "Calculate Chandrayaan-3 lander module mass: {0}",
                "Determine Vikram lander net dry mass: {0}",
                "Compute lunar daylight operational duration: {0}",
                "Calculate Aditya-L1 distance percentage: {0}",
                "Compute solar photon transit time to L1: {0}",
                "Determine lunar powered descent deceleration: {0}",
                "Compute Pragyan rover roving duration: {0}",
                "Calculate Mangalyaan interplanetary cost efficiency: {0}",
                "Determine Gaganyaan orbital period: {0}",
                "Calculate astronaut weight on lunar surface: {0}"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Formula and Given Quantities**\\nExtract masses, distances, times, speeds, or gravity parameters from the problem.\\n**Step 2: Arithmetic Evaluation**\\nCompute differences, speed/time ratios (\\(t = \\frac{{d}}{{v}}\\)), or lunar weight \\(W = mg_m\\).\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)


def gen_20_1_3():
    tc = "MH-9-SCIT-20-20.1.3"
    tname = "Atomic & Defense Research: BARC (Homi Bhabha), DRDO (APJ Abdul Kalam), TIFR, CSIR labs"
    archs = [
        # Arch 0: Homi J. Bhabha & Tata Institute of Fundamental Research (TIFR)
        {
            'data': [
                ("the brilliant nuclear physicist revered as the 'Father of the Indian Nuclear Program'", "Dr. Homi Jehangir Bhabha", "Dr. Vikram Sarabhai", "Dr. APJ Abdul Kalam", "Dr. Raja Ramanna"),
                ("the premier research institute in Mumbai founded in June 1945 by Dr. Homi Bhabha with financial support from the Sir Dorabji Tata Trust", "Tata Institute of Fundamental Research (TIFR, Mumbai)", "BARC", "IIT Bombay", "IISc Bengaluru"),
                ("the three-stage nuclear power program formulated by Dr. Homi Bhabha was strategically designed to exploit India's vast natural reserves of", "Thorium (found in monazite beach sands of Kerala and Tamil Nadu)", "Uranium-235", "Petroleum oil", "Anthracite coal"),
                ("the three sequential stages of the Indian nuclear power program formulated by Dr. Homi Bhabha", "Stage 1: PHWR (Natural Uranium); Stage 2: FBR (Plutonium); Stage 3: Advanced Heavy Water Reactors (Thorium-U233)", "Stage 1: Coal; Stage 2: Solar; Stage 3: Nuclear", "Stage 1: Thorium; Stage 2: Uranium; Stage 3: Hydrogen", "Stage 1: Fusion; Stage 2: Fission; Stage 3: Solar"),
                ("the first research nuclear reactor in Asia that attained criticality on August 4, 1956 at Trombay, Mumbai", "Apsara (swimming pool reactor)", "Cirus", "Dhruva", "Kamini"),
                ("the British physicist who served as Dr. Homi Bhabha's doctoral mentor at Cambridge University when Bhabha discovered electron-positron scattering (Bhabha Scattering)", "Paul Dirac (and Ralph Fowler)", "Ernest Rutherford", "Niels Bohr", "James Chadwick"),
                ("the relativistic quantum collision process in theoretical physics named after Dr. Homi Bhabha describing electron-positron elastic scattering", "Bhabha Scattering", "Compton Scattering", "Rutherford Scattering", "Raman Scattering"),
                ("the Atomic Energy Commission of India (AEC) was established in August 1948 under the Department of Scientific Research with its first chairman as", "Dr. Homi J. Bhabha", "Dr. Shanti Swarup Bhatnagar", "Dr. Meghnad Saha", "Sir C.V. Raman"),
                ("the tragic demise of Dr. Homi Bhabha occurred on January 24, 1966 when", "Air India Flight 101 crashed near Mont Blanc in the Alps while en route to Vienna", "He suffered a heart attack in Trombay", "He died in a laboratory fire", "He was lost in a submarine accident"),
                ("the research reactor at Kalpakkam that is the world's only operating nuclear reactor fueled entirely by man-made Uranium-233", "Kamini (Kalpakkam Mini reactor)", "Dhruva", "Apsara", "Zorlina")
            ],
            'tmpls': [
                "Which renowned theoretical physicist is celebrated as: {0}?",
                "Which flagship fundamental research institution is defined as: {0}?",
                "Which vast domestic mineral fuel strategic reserve explains: {0}?",
                "What sequential nuclear technological progression constitutes: {0}?",
                "Which historic maiden Asian nuclear reactor corresponds to: {0}?",
                "Which Nobel laureate mentor guided Dr. Bhabha in: {0}?",
                "Which relativistic quantum scattering phenomenon is named as: {0}?",
                "Who was appointed as the inaugural chairman of: {0}?",
                "What tragic international aviation disaster caused: {0}?",
                "Which unique thorium-cycle Uranium-233 reactor represents: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Indian Nuclear History Context**\\nThe statement details {item[0]}.\\n**Step 2: Homi Bhabha's Visionary Architecture**\\nBhabha founded TIFR and AEET (BARC); designed the 3-stage program transitioning natural Uranium to Thorium-U233 via Fast Breeder Reactors.\\n**Step 3: Verification**\\nThe matching institution or scientist is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 1: Bhabha Atomic Research Centre (BARC) & Nuclear Technology
        {
            'data': [
                ("the premier multidisciplinary nuclear research center of India located at Trombay, Mumbai, renamed in 1967 in honor of Dr. Homi Bhabha", "Bhabha Atomic Research Centre (BARC)", "TIFR", "IGCAR", "RRCAT"),
                ("the high-flux research reactor commissioned at BARC in 1985 that produces medical radioisotopes and weapons-grade material", "Dhruva reactor (100 MW thermal)", "Apsara", "Cirus", "Kamini"),
                ("the specialized center of the Department of Atomic Energy located at Kalpakkam, Tamil Nadu dedicated to Fast Breeder Reactor development", "Indira Gandhi Centre for Atomic Research (IGCAR)", "BARC", "NFC Hyderabad", "RRCAT Indore"),
                ("the commercial public sector undertaking that operates all civilian commercial nuclear power plants in India (e.g., Tarapur, Kudankulam, Kaiga)", "Nuclear Power Corporation of India Limited (NPCIL)", "BHEL", "NTPC", "BARC"),
                ("India's first commercial nuclear power station commissioned in October 1969 located in Palghar district, Maharashtra", "Tarapur Atomic Power Station (TAPS)", "Rawatbhata", "Kudankulam", "Narora"),
                ("the code name given to India's first peaceful nuclear test conducted underground at Pokhran, Rajasthan on May 18, 1974", "Smiling Buddha (Operation Happy Krishna)", "Operation Shakti", "Operation Vijay", "Operation Meghdoot"),
                ("the series of five underground nuclear tests conducted by India at Pokhran on May 11 and 13, 1998, establishing India as a nuclear weapons state", "Operation Shakti (Pokhran-II, National Technology Day is celebrated on May 11)", "Operation Smiling Buddha", "Operation Blue Star", "Operation Parakram"),
                ("the radioisotope widely produced by BARC used in external beam teletherapy for the radiation treatment of cancer patients", "Cobalt-60 (\\(^{60}\\text{Co}\\))", "Iodine-131", "Carbon-14", "Uranium-238"),
                ("the nuclear fuel manufacturing complex of the Department of Atomic Energy located in Hyderabad, Telangana", "Nuclear Fuel Complex (NFC, Hyderabad)", "BARC Mumbai", "Heavy Water Board", "Uranium Corporation of India"),
                ("the public sector enterprise located in Jaduguda, Jharkhand that mines and mills natural uranium ores in India", "Uranium Corporation of India Limited (UCIL)", "Coal India", "NMDC", "SAIL")
            ],
            'tmpls': [
                "Which multidisciplinary nuclear establishment is defined as: {0}?",
                "Which high-flux national research reactor corresponds to: {0}?",
                "Which fast breeder research center is located at: {0}?",
                "Which public sector nuclear operator runs: {0}?",
                "Identify India's inaugural commercial nuclear plant: {0}.",
                "What historic code name designated: {0}?",
                "Which decisive nuclear test series corresponds to: {0}?",
                "Which medical radiotherapy isotope corresponds to: {0}?",
                "Which nuclear fuel fabrication complex represents: {0}?",
                "Which domestic uranium mining corporation corresponds to: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: BARC and Nuclear Infrastructure Context**\\nThe prompt examines {item[0]}.\\n**Step 2: Nuclear Capabilities and Milestones**\\nBARC Trombay oversees nuclear science; Pokhran-I (1974) and Pokhran-II (1998) established strategic deterrence; NPCIL manages commercial reactors like Tarapur.\\n**Step 3: Verification**\\nThe matching entity is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 2: DRDO, APJ Abdul Kalam & Missile Technology (IGMDP)
        {
            'data': [
                ("the premier agency under the Ministry of Defence responsible for military research, development, and defense systems in India, formed in 1958", "Defence Research and Development Organisation (DRDO)", "ISRO", "CSIR", "HAL"),
                ("the eminent aerospace scientist and 11th President of India universally celebrated as the 'Missile Man of India'", "Dr. APJ Abdul Kalam", "Dr. Homi Bhabha", "Dr. Vikram Sarabhai", "Dr. Raja Ramanna"),
                ("the ambitious national defense program launched in 1983 led by Dr. APJ Abdul Kalam to achieve self-reliance in missile technology", "Integrated Guided Missile Development Programme (IGMDP)", "Project Devil", "Project Valiant", "Make in India Defense"),
                ("the five distinct missile systems successfully developed under the IGMDP (acronym PATNA)", "Prithvi, Agni, Trishul, Nag, and Akash", "BrahMos, Astra, Nirbhay, Shaurya, and Prahaar", "Pinaka, Tejas, Arjun, Dhruv, and Rudra", "Dhanush, K-15, Sagarika, Helina, and Sant"),
                ("India's first indigenous short-range surface-to-surface tactical ballistic missile developed under IGMDP successfully test-fired in 1988", "Prithvi missile", "Agni-I", "Akash", "Nag"),
                ("the family of medium to intercontinental range strategic nuclear-capable ballistic missiles developed by DRDO (Agni-I through Agni-V)", "Agni missile series (Agni-V has a range exceeding 5,000 km)", "Prithvi series", "BrahMos series", "Trishul series"),
                ("the anti-tank guided missile (ATGM) developed by DRDO featuring fire-and-forget capability and top-attack imaging infrared guidance", "Nag missile (helicopter-launched variant is Helina / Dhruvastra)", "Trishul", "Akash", "Prithvi"),
                ("the medium-range mobile surface-to-air missile defense system developed by DRDO capable of neutralizing multi-target aerial threats simultaneously", "Akash missile system", "Nag missile", "Prithvi missile", "K-4 missile"),
                ("the world's fastest supersonic cruise missile developed jointly by India (DRDO) and Russia (NPO Mashinostroyeniya), named after two rivers", "BrahMos (named after the Brahmaputra and Moskva rivers)", "Nirbhay", "Tomahawk", "Harpoon"),
                ("the indigenous single-engine, delta-wing multirole Light Combat Aircraft (LCA) developed by Aeronautical Development Agency (ADA) and manufactured by HAL", "LCA Tejas", "Sukhoi Su-30MKI", "MiG-21", "Mirage 2000")
            ],
            'tmpls': [
                "Which apex military research organization is defined as: {0}?",
                "Which beloved aerospace visionary is celebrated as: {0}?",
                "Which foundational defense missile program was led by: {0}?",
                "Which five cornerstone missile systems correspond to: {0}?",
                "Which maiden tactical surface ballistic missile represents: {0}?",
                "Which strategic intercontinental ballistic missile family corresponds to: {0}?",
                "Which fire-and-forget anti-tank missile represents: {0}?",
                "Which multi-target surface-to-air defense shield corresponds to: {0}?",
                "Which supreme supersonic cruise missile represents: {0}?",
                "Which indigenous delta-wing light fighter jet matches: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: DRDO and Defense Missiles Context**\\nThe statement details {item[0]}.\\n**Step 2: IGMDP Missile Classes**\\nPATNA: Prithvi (surface-surface), Agni (strategic ballistic), Trishul (short-range SAM), Nag (anti-tank), Akash (medium SAM); BrahMos is supersonic cruise missile.\\n**Step 3: Verification**\\nThe matching defense weapon or entity is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 3: Council of Scientific and Industrial Research (CSIR) & National Labs
        {
            'data': [
                ("the largest autonomous civil research and development organization in India established in September 1942, operating a nationwide network of 37 laboratories", "Council of Scientific and Industrial Research (CSIR)", "DRDO", "ICMR", "ICAR"),
                ("the pioneering physical chemist who served as the first Director General of CSIR, after whom India's highest annual science award is named", "Dr. Shanti Swarup Bhatnagar", "Dr. Meghnad Saha", "Dr. Birbal Sahni", "Dr. CV Raman"),
                ("the prestigious annual prize awarded by CSIR recognizing outstanding Indian scientists under 45 years of age across seven disciplines", "Shanti Swarup Bhatnagar Prize for Science and Technology", "Bharat Ratna", "Padma Vibhushan", "Infosys Prize"),
                ("the premier CSIR laboratory located in Pune, Maharashtra renowned for chemical synthesis, catalysis, polymers, and green chemistry", "CSIR-National Chemical Laboratory (NCL, Pune)", "CSIR-NPL New Delhi", "CSIR-CCMB Hyderabad", "CSIR-CDRI Lucknow"),
                ("the premier CSIR laboratory located in New Delhi responsible for maintaining the National Physical Standards of measurement and Indian Standard Time (IST)", "CSIR-National Physical Laboratory (NPL, New Delhi)", "CSIR-NCL Pune", "CSIR-CSIO Chandigarh", "CSIR-NAL Bengaluru"),
                ("the purple indelible ink applied to voters' fingernails during democratic elections in India to prevent fraudulent double voting, formulated by CSIR-NPL", "Indelible voter ink (containing silver nitrate, \\(AgNO_3\\))", "Gentian violet dye", "Potassium permanganate", "Methylene blue"),
                ("the premier CSIR laboratory located in Hyderabad, Telangana dedicated to molecular biology, genomics, cellular processes, and DNA fingerprinting", "CSIR-Centre for Cellular and Molecular Biology (CCMB, Hyderabad)", "CSIR-CDRI Lucknow", "CSIR-CFTRI Mysuru", "CSIR-IGIB Delhi"),
                ("the premier CSIR laboratory located in Lucknow, Uttar Pradesh responsible for discovering new pharmaceutical drugs (e.g., Centchroman / Saheli)", "CSIR-Central Drug Research Institute (CDRI, Lucknow)", "CSIR-NCL Pune", "CSIR-IICB Kolkata", "CSIR-NEIST Jorhat"),
                ("the premier CSIR laboratory located in Mysuru, Karnataka specializing in food processing technologies, preservation, and nutrition security", "CSIR-Central Food Technological Research Institute (CFTRI, Mysuru)", "CSIR-NCL Pune", "CSIR-CDRI Lucknow", "CSIR-AMPRI Bhopal"),
                ("the aerospace laboratory of CSIR located in Bengaluru that developed the Saras civil passenger aircraft and Hansa trainer aircraft", "CSIR-National Aerospace Laboratories (NAL, Bengaluru)", "HAL", "DRDO", "ADA")
            ],
            'tmpls': [
                "Which massive civil scientific research network is defined as: {0}?",
                "Name the founding director general associated with: {0}.",
                "Which apex domestic scientific accolade corresponds to: {0}?",
                "Which chemical research institute represents: {0}?",
                "Which metrological standard-bearer institute corresponds to: {0}?",
                "Which democratic electoral chemical invention represents: {0}?",
                "Which genomic and molecular institute corresponds to: {0}?",
                "Which pharmaceutical drug discovery laboratory matches: {0}?",
                "Which food technology research institute represents: {0}?",
                "Which civil aeronautical laboratory developed: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: CSIR Network Context**\\nThe query highlights {item[0]}.\\n**Step 2: National Labs and Inventions**\\nCSIR was founded by Dr. SS Bhatnagar; NCL leads in chemistry, NPL maintains IST and voting ink (\\(AgNO_3\\)), CCMB excels in genomics, and CDRI discovers drugs.\\n**Step 3: Verification**\\nThe matching institution or achievement is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 4: Advanced Defense Platforms: Arihant, Tejas, Pinaka & Radar
        {
            'data': [
                ("India's first indigenous nuclear-powered ballistic missile submarine (SSBN) commissioned in 2016, completing India's strategic nuclear triad", "INS Arihant (S2)", "INS Vikrant", "INS Kalvari", "INS Chakra"),
                ("the strategic military doctrine where a nation possesses the capability to launch retaliatory nuclear strikes from land, air, and sea", "Nuclear Triad (Land-based missiles, strategic bombers, and SSBN submarines)", "First strike doctrine", "Mutually Assured Peace", "Non-proliferation treaty"),
                ("India's first indigenously designed and built aircraft carrier commissioned into the Indian Navy in September 2022, built by Cochin Shipyard", "INS Vikrant (IAC-1)", "INS Vikramaditya", "INS Viraat", "INS Vishal"),
                ("the multi-barrel rocket artillery launcher system developed by DRDO capable of firing 12 high-explosive rockets in 44 seconds up to 40-75 km", "Pinaka Multi-Barrel Rocket Launcher (MBRL)", "BM-21 Grad", "Smerch", "HIMARS"),
                ("the main battle tank (MBT) designed and developed by DRDO featuring Kanchan composite armor and a 120 mm rifled gun", "Arjun MBT", "T-90 Bhishma", "T-72 Ajeya", "Vijayanta"),
                ("the Beyond-Visual-Range (BVR) air-to-air missile developed by DRDO capable of engaging enemy fighter aircraft at ranges over 100 km", "Astra missile", "Nag missile", "Helina", "Prithvi"),
                ("the 3D radar system developed by DRDO for 3D multi-target surveillance and tracking of aircraft, drones, and missiles", "Rohini 3D radar and Swathi weapon locating radar", "Indra radar", "Rajendra radar", "Airborne Early Warning radar"),
                ("the unmanned combat aerial vehicle (UCAV) and medium-altitude long-endurance (MALE) drone developed by DRDO for military reconnaissance", "Rustom-II (Tapas-BH-201)", "Nishant", "Lakshya", "Abhyas"),
                ("the anti-satellite weapon test conducted by DRDO on March 27, 2019 (Mission Shakti) that successfully destroyed a live satellite in Low Earth Orbit", "Mission Shakti (Anti-Satellite / ASAT test)", "Operation Shakti", "Mission Sagar", "Operation Rahat"),
                ("the supersonic surface-to-air missile defense system developed by DRDO to intercept incoming hostile ballistic missiles in the atmosphere (AAD / PAD)", "Ballistic Missile Defence (BMD) shield (Prithvi Air Defence and Advanced Air Defence)", "Akash SAM", "Trishul SAM", "S-400 Triumf")
            ],
            'tmpls': [
                "Which indigenous nuclear submarine milestone is defined as: {0}?",
                "Which comprehensive strategic military deterrent represents: {0}?",
                "Which maiden indigenous aircraft carrier corresponds to: {0}?",
                "Which rapid multi-barrel rocket artillery system represents: {0}?",
                "Which indigenous main battle tank is characterized by: {0}?",
                "Which beyond-visual-range air combat missile matches: {0}?",
                "Which advanced 3D surveillance radar corresponds to: {0}?",
                "Which indigenous long-endurance military drone represents: {0}?",
                "Which historic space deterrence weapon test represents: {0}?",
                "Which strategic multi-tier ballistic missile shield corresponds to: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Defense Platform Engineering Context**\\nThe statement details {item[0]}.\\n**Step 2: Strategic Deterrence Systems**\\nINS Arihant completed the Nuclear Triad; Pinaka provides artillery saturation; Astra provides BVR air superiority; Mission Shakti proved ASAT capability.\\n**Step 3: Verification**\\nThe matching defense system is {item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 5: Medical, Agricultural & Industrial Applications of Radiation
        {
            'data': [
                ("the technique of using controlled doses of ionizing radiation (gamma rays or electron beams) to kill food pathogens and extend shelf life", "Food irradiation (using Cobalt-60 or Cesium-137 at BARC facilities)", "Thermal pasteurization", "Chemical canning", "Freeze drying"),
                ("the agricultural mutation breeding technique developed by BARC that created high-yielding, disease-resistant crop varieties across India", "Trombay mutant varieties (e.g., Trombay groundnut TG-series, black gram, mung bean)", "Organic permaculture", "Chemical hybridization", "Hydroponic cloning"),
                ("the radioisotope of iodine widely used in nuclear medicine for diagnosing and treating thyroid cancer and hyperthyroidism", "Iodine-131 (\\(^{131}\\text{I}\\))", "Cobalt-60", "Technetium-99m", "Phosphorus-32"),
                ("the short-lived metastable radioisotope produced in nuclear medicine that is the most widely used diagnostic imaging tracer in human hospitals", "Technetium-99m (\\(^{99m}\\text{Tc}\\), half-life of 6 hours)", "Carbon-14", "Uranium-235", "Radium-226"),
                ("the industrial non-destructive testing (NDT) method using gamma radiation from Iridium-192 to inspect welds in high-pressure oil pipelines and aircraft", "Industrial gamma radiography", "Ultrasonic cleaning", "Chemical etching", "Magnetic levitation"),
                ("the radiocarbon dating method developed by Willard Libby in 1949 that determines the age of ancient organic archaeological artifacts using", "Carbon-14 radioactive decay (half-life of 5,730 years)", "Uranium-238 decay", "Potassium-40 dating", "Lead isotope ratio"),
                ("the specialized hospital facility operated by the Department of Atomic Energy in Mumbai providing comprehensive cancer care and research", "Tata Memorial Hospital (TMH, Mumbai)", "AIIMS New Delhi", "Apollo Hospitals", "Fortis Healthcare"),
                ("the nuclear technique using radiation to sterilize male insect pests (e.g., screwworm, fruit fly) to eradicate insect populations without chemical pesticides", "Sterile Insect Technique (SIT)", "Chemical pesticide spraying", "Biological predation", "Genetic cloning"),
                ("the radioactive isotope used in residential smoke detectors to ionize air molecules inside the sensing chamber", "Americium-241 (\\(^{241}\\text{Am}\\))", "Plutonium-239", "Uranium-235", "Radium-226"),
                ("the desalination demonstration plant established by BARC at Kalpakkam utilizing waste steam from nuclear reactors to produce fresh drinking water", "Nuclear desalination plant (multi-stage flash evaporation and RO)", "Solar distillation still", "Chemical precipitation plant", "Electrolysis unit")
            ],
            'tmpls': [
                "Which radio-preservation technique is defined as: {0}?",
                "Which nuclear agricultural breeding program represents: {0}?",
                "Which thyroid therapeutic radioisotope corresponds to: {0}?",
                "Which universal diagnostic nuclear tracer represents: {0}?",
                "Which industrial non-destructive inspection method represents: {0}?",
                "Which foundational archaeological dating method uses: {0}?",
                "Which renowned oncology hospital is operated by: {0}?",
                "Which environmentally safe pest eradication technique represents: {0}?",
                "Which domestic ionizing smoke detection isotope corresponds to: {0}?",
                "Which coastal nuclear freshwater production facility represents: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Radioisotope Applications Context**\\nThe prompt examines {item[0]}.\\n**Step 2: Peaceful Uses of Atomic Energy**\\nBARC utilizes radiation for crop mutations (Trombay seeds), food preservation (Cobalt-60), cancer treatment (Cobalt-60, Iodine-131, Technetium-99m), and desalination.\\n**Step 3: Verification**\\nThe matching application is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 6: Nobel Laureates & Indian Scientific Institutions (ICMR, ICAR, TIFR)
        {
            'data': [
                ("the premier Indian medical research organization established in 1911 responsible for formulation, coordination, and promotion of biomedical research", "Indian Council of Medical Research (ICMR, New Delhi)", "CSIR", "DRDO", "BARC"),
                ("the apex national agricultural research body in India overseeing 101 institutes that spearheaded the Green Revolution in Indian farming", "Indian Council of Agricultural Research (ICAR, New Delhi)", "CSIR", "ICMR", "FSSAI"),
                ("the renowned geneticist and agricultural scientist widely acclaimed as the 'Father of the Green Revolution in India' who passed away in 2023", "Dr. M.S. Swaminathan", "Dr. Norman Borlaug", "Dr. Verghese Kurien", "Dr. Homi Bhabha"),
                ("the visionary social engineer and dairy technologist celebrated as the 'Father of the White Revolution in India' and architect of Operation Flood", "Dr. Verghese Kurien (founder of Amul)", "Dr. M.S. Swaminathan", "Dr. APJ Abdul Kalam", "Dr. Vikram Sarabhai"),
                ("the world's largest agricultural dairy development program launched in 1970 that transformed India from a milk-deficient nation into the world's largest milk producer", "Operation Flood (White Revolution)", "Green Revolution", "Blue Revolution", "Yellow Revolution"),
                ("the Indian-origin astrophysicist who won the 1983 Nobel Prize in Physics for mathematical theories on the physical structure and evolution of stars", "Subrahmanyan Chandrasekhar (Chandrasekhar Limit = 1.44 solar masses)", "Sir C.V. Raman", "Dr. Homi Bhabha", "Prof. Satyendra Nath Bose"),
                ("the Indian-born biochemist who shared the 1968 Nobel Prize in Physiology or Medicine for cracking the genetic code and synthesizing artificial genes", "Har Gobind Khorana", "Venkatraman Ramakrishnan", "C.V. Raman", "Amartya Sen"),
                ("the Indian-born structural biologist who won the 2009 Nobel Prize in Chemistry for mapping the atomic structure and function of the ribosome", "Venkatraman 'Venki' Ramakrishnan", "Har Gobind Khorana", "C.V. Raman", "S. Chandrasekhar"),
                ("the premier science university established in Bengaluru in 1909 envisioned by Jamsetji Tata and Swami Vivekananda", "Indian Institute of Science (IISc Bengaluru)", "IIT Bombay", "TIFR Mumbai", "JNU New Delhi"),
                ("the first Indian Director of the Indian Institute of Science (IISc Bengaluru), appointed in 1933", "Sir C.V. Raman", "Dr. Homi Bhabha", "Satish Dhawan", "C.N.R. Rao")
            ],
            'tmpls': [
                "Which apex national biomedical research body is defined as: {0}?",
                "Which apex agricultural research establishment corresponds to: {0}?",
                "Which renowned agronomist is celebrated as: {0}?",
                "Which dairy visionary is recognized as: {0}?",
                "Which historic dairy development program represents: {0}?",
                "Which Nobel laureate astrophysicist is celebrated for: {0}?",
                "Which Nobel laureate molecular biochemist corresponds to: {0}?",
                "Which Nobel laureate structural biologist is celebrated for: {0}?",
                "Which premier century-old science university corresponds to: {0}?",
                "Who served as the historic first Indian director of: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Indian Scientific Leaders Context**\\nThe statement details {item[0]}.\\n**Step 2: Nobel Laureates and Revolution Architects**\\nChandrasekhar (Chandrasekhar Limit), Khorana (Genetic Code), Ramakrishnan (Ribosome structure), MS Swaminathan (Green Revolution), and Kurien (White Revolution).\\n**Step 3: Verification**\\nThe correct scientific leader is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 7: Quantitative Problems in Nuclear Fission, Half-Life & Range
        {
            'data': [
                ("A radioactive sample of Iodine-131 (half-life \\(T_{1/2} = 8\\text{ days}\\)) has an initial mass of \\(40\\text{ mg}\\). Calculate the mass of Iodine-131 remaining undecayed after \\(24\\text{ days}\\) (\\(3\\text{ half-lives}\\)).", "\\(5.0\\text{ mg } (\\frac{40}{2^3} = 5.0\\text{ mg})\\)", "\\(10.0\\text{ mg}\\)", "\\(2.5\\text{ mg}\\)", "\\(20.0\\text{ mg}\\)"),
                ("Technetium-99m has a radioactive half-life of \\(6\\text{ hours}\\). If a patient is injected with a dose of \\(800\\text{ MBq}\\), what radioactive activity remains in the body after \\(18\\text{ hours}\\)?", "\\(100\\text{ MBq } (\\frac{800}{2^3} = 100\\text{ MBq})\\)", "\\(200\\text{ MBq}\\)", "\\(50\\text{ MBq}\\)", "\\(400\\text{ MBq}\\)"),
                ("In a nuclear fission reaction of one Uranium-235 nucleus, approximately \\(200\\text{ MeV}\\) of energy is released. Taking \\(1\\text{ eV} = 1.6 \\times 10^{-19}\\text{ J}\\), calculate the energy released per fission event in Joules.", "\\(3.2 \\times 10^{-11}\\text{ Joules}\\)", "\\(1.6 \\times 10^{-13}\\text{ J}\\)", "\\(3.2 \\times 10^{-19}\\text{ J}\\)", "\\(6.4 \\times 10^{-8}\\text{ J}\\)"),
                ("Calculate the theoretical energy released by the complete nuclear conversion of \\(1\\text{ gram } (10^{-3}\\text{ kg})\\) of matter using Einstein's mass-energy equation \\(E = mc^2\\) (\\(c = 3 \\times 10^8\\text{ m/s}\\)).", "\\(9.0 \\times 10^{13}\\text{ Joules } (90\\text{ Terajoules})\\)", "\\(3.0 \\times 10^8\\text{ J}\\)", "\\(9.0 \\times 10^{16}\\text{ J}\\)", "\\(1.0 \\times 10^{10}\\text{ J}\\)"),
                ("A BrahMos supersonic cruise missile flies at a speed of Mach 2.8. Taking the speed of sound in air as \\(340\\text{ m/s } (1224\\text{ km/h})\\), calculate the speed of the BrahMos missile in \\(\\text{km/h}\\).", "\\(3427.2\\text{ km/h } (2.8 \\times 1224\\text{ km/h})\\)", "\\(2400.0\\text{ km/h}\\)", "\\(1224.0\\text{ km/h}\\)", "\\(4500.0\\text{ km/h}\\)"),
                ("An Agni-V intercontinental ballistic missile travels a distance of \\(5000\\text{ km}\\) at an average re-entry velocity of \\(6.0\\text{ km/s}\\). How many minutes does the missile take to complete its flight trajectory?", "\\(13.89\\text{ minutes } (\\approx 14\\text{ minutes})\\)", "\\(30.0\\text{ minutes}\\)", "\\(60.0\\text{ minutes}\\)", "\\(5.0\\text{ minutes}\\)"),
                ("The Tarapur Atomic Power Station has two operating PHWR units producing \\(540\\text{ MWe}\\) each. Calculate the total combined electrical power capacity in Megawatts.", "\\(1080\\text{ MWe } (1.08\\text{ GWe})\\)", "\\(540\\text{ MWe}\\)", "\\(2000\\text{ MWe}\\)", "\\(750\\text{ MWe}\\)"),
                ("In carbon dating, an ancient wooden relic contains \\(25\\%\\) of the Carbon-14 activity of living wood. If the half-life of Carbon-14 is \\(5730\\text{ years}\\), calculate the estimated age of the archaeological relic.", "\\(11,460\\text{ years } (2 \\text{ half-lives})\\)", "\\(5,730\\text{ years}\\)", "\\(17,190\\text{ years}\\)", "\\(2,865\\text{ years}\\)"),
                ("The Pinaka multi-barrel rocket launcher fires \\(12\\text{ rockets}\\) in \\(44\\text{ seconds}\\). What is the average time interval between consecutive rocket launches?", "\\(4.0\\text{ seconds } (\\frac{44}{11} = 4.0\\text{ s})\\)", "\\(3.67\\text{ seconds}\\)", "\\(5.0\\text{ seconds}\\)", "\\(2.0\\text{ seconds}\\)"),
                ("The Chandrasekhar Limit defines the maximum mass of a stable white dwarf star as \\(1.44\\) times the mass of the Sun (\\(M_\\odot = 2 \\times 10^{30}\\text{ kg}\\)). Calculate this limiting mass in kilograms.", "\\(2.88 \\times 10^{30}\\text{ kg}\\)", "\\(1.44 \\times 10^{30}\\text{ kg}\\)", "\\(5.76 \\times 10^{30}\\text{ kg}\\)", "\\(1.00 \\times 10^{31}\\text{ kg}\\)")
            ],
            'tmpls': [
                "Calculate residual radioisotope mass after decay: {0}",
                "Determine clinical radiotracer activity: {0}",
                "Compute nuclear fission energy liberation in Joules: {0}",
                "Evaluate Einstein mass-energy conversion output: {0}",
                "Calculate supersonic Mach cruise velocity in km/h: {0}",
                "Determine ballistic missile flight time duration: {0}",
                "Compute total nuclear generating capacity: {0}",
                "Calculate archaeological radiocarbon age: {0}",
                "Evaluate rocket artillery launch interval: {0}",
                "Compute Chandrasekhar stellar mass threshold: {0}"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Formula and Given Quantities**\\nExtract half-lives, speeds, powers, or mass parameters from the problem.\\n**Step 2: Arithmetic Evaluation**\\nApply \\(N = N_0(1/2)^n\\), \\(E = mc^2\\), \\(v = \\text{{Mach}} \\times v_{{\\text{{sound}}}}\\), or \\(t = \\frac{{d}}{{v}}\\).\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)


def gen_20_1_4():
    tc = "MH-9-SCIT-20-20.1.4"
    tname = "Astronomical facilities in India: GMRT (Pune), IUCAA, ARIES Nainital, Hanle Observatory Ladakh"
    archs = [
        # Arch 0: Giant Metrewave Radio Telescope (GMRT, Khodad-Pune)
        {
            'data': [
                ("the world-class low-frequency radio astronomical observatory located at Khodad near Narayangaon, Pune, operated by NCRA-TIFR", "Giant Metrewave Radio Telescope (GMRT)", "Hanle Observatory", "ARIES Nainital", "Ooty Radio Telescope"),
                ("the unique structural configuration of the Giant Metrewave Radio Telescope (GMRT) array", "30 fully steerable parabolic radio dish antennas, each with a diameter of 45 metres, spread over a 25 km baseline in a Y-shaped array", "One single 500-metre giant dish", "100 small optical mirrors", "A single underground neutrino tank"),
                ("the innovative lightweight antenna design concept invented by Prof. Govind Swarup for GMRT's 45-metre dish antennas", "Stretched wire mesh SMART (Stressed Mesh Antenna Research Technology) surface", "Solid heavy cast iron plates", "Polished aluminum mirrors", "Titanium alloy plates"),
                ("the visionary radio astronomer regarded as the 'Father of Indian Radio Astronomy' who spearheaded the creation of the Ooty Radio Telescope and GMRT", "Prof. Govind Swarup", "Prof. Jayant Narlikar", "Dr. Homi Bhabha", "Dr. Vikram Sarabhai"),
                ("the prestigious international scientific recognition awarded to GMRT in 2021 by the Institute of Electrical and Electronics Engineers", "IEEE Milestone Award (the third IEEE Milestone in India after JC Bose and CV Raman)", "Nobel Prize", "Fields Medal", "Kyoto Prize"),
                ("the radio frequency coverage range across which the GMRT array operates (the 'metrewave' band)", "From 50 MHz to 1450 MHz (wavelengths from 6 metres to 21 cm)", "From 10 GHz to 100 GHz", "Optical infrared frequencies only", "Gamma ray frequencies"),
                ("the major astrophysical discoveries and phenomena investigated using the Giant Metrewave Radio Telescope", "Pulsars, fast radio bursts (FRBs), distant radio galaxies, magnetic fields in galaxy clusters, and the epoch of reionization (21-cm hydrogen line)", "Discovering exoplanet trees", "Measuring Earth's rainfall", "Tracking aircraft flight paths"),
                ("the primary astronomical organization headquartered inside the Savitribai Phule Pune University campus that operates the GMRT", "National Centre for Radio Astrophysics (NCRA-TIFR, Pune)", "IUCAA", "ISRO", "PRL Ahmedabad"),
                ("the historic large cylindrical parabolic radio telescope constructed on a natural hill slope at Muthorai near Ooty in 1970", "Ooty Radio Telescope (ORT, 530 m long and 30 m wide)", "GMRT", "Hanle Telescope", "Devasthal Optical Telescope"),
                ("why the Ooty Radio Telescope was deliberately constructed on a natural north-south hillside sloping at 11 degrees", "The hill slope matches the latitude of the station, allowing the telescope to track celestial objects for 9.5 hours simply by rotating around its long axis", "To avoid rainwater pooling", "To keep it hidden from radar", "To make maintenance easier")
            ],
            'tmpls': [
                "Which world-renowned radio observatory is defined as: {0}?",
                "Describe the multi-dish architectural configuration: {0}.",
                "Which innovative lightweight antenna engineering represents: {0}?",
                "Name the renowned visionary astronomer celebrated as: {0}.",
                "Which prestigious international engineering accolade was awarded to: {0}?",
                "What electromagnetic frequency spectrum band characterizes: {0}?",
                "What frontline deep-space astrophysical discoveries are made by: {0}?",
                "Which premier radio astrophysics institute operates: {0}?",
                "Which historic 530-metre cylindrical radio facility corresponds to: {0}?",
                "What latitude celestial tracking alignment explains why: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: GMRT and Radio Astronomy Context**\\nThe statement details {item[0]}.\\n**Step 2: Engineering Innovation and Science**\\nProf. Govind Swarup designed GMRT (30 dishes of 45 m in Y-array using stretched wire mesh) operating from 50 to 1450 MHz; awarded IEEE Milestone in 2021.\\n**Step 3: Verification**\\nThe matching observatory or entity is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 1: Inter-University Centre for Astronomy and Astrophysics (IUCAA, Pune)
        {
            'data': [
                ("the autonomous academic institution located on Pune University campus dedicated to promoting astronomy research and education across Indian universities", "Inter-University Centre for Astronomy and Astrophysics (IUCAA)", "NCRA", "TIFR", "ARIES"),
                ("the world-renowned theoretical cosmologist and science writer who served as the founder-director of IUCAA in 1988", "Prof. Jayant Vishnu Narlikar", "Prof. Govind Swarup", "Dr. Homi Bhabha", "Prof. CNR Rao"),
                ("the non-standard cosmological theory formulated by Sir Fred Hoyle and Prof. Jayant Narlikar in 1964 as an alternative to the Big Bang", "Hoyle-Narlikar Theory of Gravity (Conformal Gravity / Quasi-Steady State Cosmology)", "General Theory of Relativity", "String Theory", "Quantum Loop Gravity"),
                ("the 2-metre optical and near-infrared telescope operated by IUCAA located at Girawali near Junnar in Pune district", "IUCAA Girawali Observatory (IGO)", "Devasthal Telescope", "Himalayan Chandra Telescope", "Vainu Bappu Telescope"),
                ("the beloved science popularizer and toy inventor who headed the Children's Science Centre at IUCAA creating low-cost toys from trash", "Arvind Gupta (Padma Shri recipient)", "Prof. Jayant Narlikar", "Dr. APJ Abdul Kalam", "Prof. Yash Pal"),
                ("the monumental international astrophysics project where IUCAA leads the Indian scientific consortium to construct an advanced gravitational wave detector in India", "LIGO-India (Laser Interferometer Gravitational-Wave Observatory)", "Square Kilometre Array (SKA)", "Thirty Metre Telescope", "Event Horizon Telescope"),
                ("the district in Maharashtra officially selected and approved for constructing the multi-billion rupee LIGO-India gravitational-wave observatory", "Hingoli district (Aundha Nagnath)", "Pune district", "Nagpur district", "Kolhapur district"),
                ("the payload aboard ISRO's Aditya-L1 solar mission whose scientific design and development was led by IUCAA scientists", "SUIT (Solar Ultraviolet Imaging Telescope)", "VELC", "PAPA", "ASPEX"),
                ("the fundamental celestial phenomenon predicted by Albert Einstein in 1916 that LIGO-India will detect as ripples in spacetime", "Gravitational waves (generated by merging black holes and neutron stars)", "Electromagnetic radio waves", "Solar wind streams", "Cosmic gamma rays"),
                ("the massive statue of which historic English physicist and mathematician adorns the central courtyard of the IUCAA campus in Pune", "Sir Isaac Newton (under a descendant of the famous apple tree)", "Albert Einstein", "Galileo Galilei", "Johannes Kepler")
            ],
            'tmpls': [
                "Which premier national astrophysics centre is defined as: {0}?",
                "Name the renowned founding cosmologist who established: {0}.",
                "Which alternative cosmological theory was co-formulated by: {0}?",
                "Which optical observatory in Pune district represents: {0}?",
                "Which grassroot science educator created: {0}?",
                "Which mega-science gravitational wave consortium is led by: {0}?",
                "Which Maharashtra district was officially selected for: {0}?",
                "Which solar ultraviolet instrument was developed by: {0}?",
                "Which spacetime ripple phenomenon will be detected by: {0}?",
                "Which iconic historical statue adorns the campus of: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: IUCAA and Astrophysics Context**\\nThe prompt examines {item[0]}.\\n**Step 2: Narlikar's Legacy and LIGO-India**\\nFounded by Prof. Jayant Narlikar; developed SUIT for Aditya-L1; leads the LIGO-India gravitational wave detector in Hingoli, Maharashtra.\\n**Step 3: Verification**\\nThe matching institution is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 2: Indian Astronomical Observatory (IAO, Hanle-Ladakh)
        {
            'data': [
                ("the world's highest ground-based optical and infrared observatory located at an altitude of 4,500 metres (14,764 ft) in eastern Ladakh", "Indian Astronomical Observatory (IAO, Hanle)", "ARIES Nainital", "Vainu Bappu Observatory", "Mount Abu Observatory"),
                ("the primary 2-metre optical and near-infrared reflecting telescope installed at the Indian Astronomical Observatory in Hanle", "Himalayan Chandra Telescope (HCT, named after Nobel laureate S. Chandrasekhar)", "Devasthal Optical Telescope", "Giant Metrewave Telescope", "Vainu Bappu Telescope"),
                ("the premier astronomical institute in Bengaluru, Karnataka that owns and operates the Indian Astronomical Observatory at Hanle", "Indian Institute of Astrophysics (IIA, Bengaluru)", "IUCAA Pune", "TIFR Mumbai", "ARIES Nainital"),
                ("how astronomers in Bengaluru operate and control the Himalayan Chandra Telescope located 3,000 km away in remote Ladakh", "Remotely via a dedicated high-speed INSAT satellite communications link from CREST, Hosakote near Bengaluru", "By traveling to Ladakh every night", "Using optical fiber cables through mountains", "Using shortwave radio Morse code"),
                ("the atmospheric and geographic conditions at Hanle, Ladakh that make it one of the premier astronomical sites in the world", "High altitude (thin atmosphere), exceptionally low atmospheric water vapor, cloudless dry desert skies (>250 clear nights/year), and zero light pollution", "Heavy snowfall that cools mirrors", "Continuous monsoon rain that washes dust", "Proximity to the equator"),
                ("the high-altitude gamma-ray Cherenkov telescope array installed at Hanle, Ladakh to study extreme cosmic gamma-ray sources", "MACE (Major Atmospheric Cherenkov Experiment Telescope, 21-metre diameter dish)", "HCT", "DOT", "GMRT"),
                ("the official designation awarded to the Hanle region in Ladakh in December 2022 to protect its pristine night skies from artificial light pollution", "Hanle Dark Sky Reserve (India's first Dark Sky Reserve)", "National Biosphere Reserve", "Tiger Sanctuary", "Solar Energy Park"),
                ("the centre established by IIA at Hosakote near Bengaluru for payload integration, space optics fabrication, and remote telescope operations", "CREST (Centre for Research and Education in Science and Technology)", "VSSC", "SAC", "NRSC"),
                ("the specialized 21-metre segmented dish telescope at Hanle that is the highest Cherenkov telescope in the world and second largest globally", "MACE telescope", "HCT", "Giant Metrewave Dish", "Ooty Cylinder"),
                ("why low ambient water vapor is essential for high-altitude infrared astronomical observations at Hanle", "Atmospheric water vapor strongly absorbs infrared radiation from deep space; dry high-altitude air opens infrared transmission windows", "Water vapor reflects radio waves", "Water vapor causes mirrors to melt", "Water vapor magnetizes starlight")
            ],
            'tmpls': [
                "Which extreme high-altitude observatory is defined as: {0}?",
                "Which 2-metre optical telescope corresponds to: {0}?",
                "Which parent astronomical institute operates: {0}?",
                "What remote tele-operation satellite link enables: {0}?",
                "What pristine atmospheric parameters explain why: {0}?",
                "Which massive gamma-ray Cherenkov telescope array represents: {0}?",
                "Which nocturnal environmental designation was awarded to: {0}?",
                "Which technological integration campus corresponds to: {0}?",
                "Which 21-metre Cherenkov collector represents: {0}?",
                "What infrared atmospheric absorption rationale explains why: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Hanle Observatory Context**\\nThe statement details {item[0]}.\\n**Step 2: High-Altitude Astronomy in Ladakh**\\nAt 4,500 m, Hanle provides dry, thin air with zero light pollution; hosts HCT (2 m) and MACE (21 m gamma-ray); designated India's first Dark Sky Reserve.\\n**Step 3: Verification**\\nThe matching observatory entity is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 3: ARIES (Nainital) & Devasthal Optical Telescope (DOT)
        {
            'data': [
                ("the premier autonomous astronomical institute under the Department of Science and Technology located at Manora Peak near Nainital, Uttarakhand", "Aryabhatta Research Institute of Observational Sciences (ARIES)", "IUCAA", "IIA", "PRL"),
                ("the 3.6-metre optical telescope commissioned at Devasthal near Nainital in 2016, which is India's largest steerable optical telescope", "3.6-metre Devasthal Optical Telescope (DOT)", "Himalayan Chandra Telescope", "Vainu Bappu Telescope", "Girawali Telescope"),
                ("the foreign country and agency that partnered with India (ARIES) to design and construct the 3.6-metre Devasthal Optical Telescope", "Belgium (Advanced Mechanical and Optical Systems - AMOS)", "Russia", "United States", "Japan"),
                ("the 4-metre liquid-mirror telescope installed at Devasthal (ILMT) that uses a rotating pool of liquid metal to survey the deep sky", "International Liquid Mirror Telescope (ILMT, uses a rotating dish of liquid mercury)", "Devasthal Optical Telescope", "HCT", "GMRT"),
                ("how a liquid mirror telescope (ILMT) creates a perfect parabolic reflecting surface without mechanical glass grinding", "A thin layer of liquid mercury placed in a container rotated at a constant speed naturally forms a perfect paraboloid under gravity and centrifugal force", "Liquid mercury is magnetized by lasers", "Mercury is frozen into solid shape", "Surface tension alone forms a sphere"),
                ("the geographical elevation of the Devasthal peak observatory site in the Kumaon Himalayas providing dark skies and sharp optical seeing", "2,450 metres (approx 8,000 feet) above sea level", "500 metres", "4,500 metres", "1,000 metres"),
                ("the astronomical optical metric 'seeing' measured at Devasthal that quantifies atmospheric turbulence and image sharpness", "Astronomical seeing (measured in arcseconds, ~0.7 arcseconds at Devasthal indicating crystal sharp seeing)", "Apparent magnitude", "Focal length", "Refractive dispersion"),
                ("the 1.3-metre wide-field optical telescope installed at Devasthal in 2010 used for observing transient gamma-ray bursts and supernovae", "1.3-metre Devasthal Fast Optical Telescope (DFOT)", "3.6-metre DOT", "ILMT", "HCT"),
                ("the high-resolution optical spectrograph installed on the 3.6-metre DOT used to discover exoplanets around distant stars via radial velocity shifts", "TANSPEC and ADFOSC (ARIES Devasthal Faint Object Spectrograph & Camera)", "MACE", "CLASS", "SUIT"),
                ("the main research disciplines pursued at ARIES Manora Peak in addition to observational astronomy", "Atmospheric sciences, aerosol measurements, and solar physics in the lower central Himalayas", "Deep sea geology", "Nuclear weapon design", "Petroleum exploration")
            ],
            'tmpls': [
                "Which Himalayan research institute is defined as: {0}?",
                "Which supreme 3.6-metre national optical telescope corresponds to: {0}?",
                "Which international European engineering partner co-built: {0}?",
                "Which unique 4-metre liquid mirror telescope represents: {0}?",
                "What fluid dynamic physics principle explains how: {0}?",
                "What geographic elevation characterizes: {0}?",
                "Which optical turbulence metric defines: {0}?",
                "Which 1.3-metre transient survey telescope corresponds to: {0}?",
                "Which faint-object spectrographic camera represents: {0}?",
                "Which complementary atmospheric science discipline is pursued at: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: ARIES and Devasthal Context**\\nThe query highlights {item[0]}.\\n**Step 2: Optical Telescopes in Kumaon**\\nARIES operates the 3.6 m DOT (India's largest steerable optical telescope) and the 4 m ILMT (rotating liquid mercury mirror) at Devasthal peak (2,450 m).\\n**Step 3: Verification**\\nThe matching facility is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 4: Solar & Optical Observatories: Udaipur, Kodaikanal & Kavalur
        {
            'data': [
                ("the solar observatory located on an island in Lake Fateh Sagar, Udaipur, Rajasthan, operated by the Physical Research Laboratory (PRL)", "Udaipur Solar Observatory (USO)", "Kodaikanal Observatory", "ARIES", "GMRT"),
                ("why the Udaipur Solar Observatory was deliberately constructed on an island surrounded by a large body of lake water", "Water has high heat capacity, suppressing air temperature fluctuations and ground heat convection currents that blur solar telescope images", "To keep the telescope cool in winter", "To collect drinking water", "To reflect solar light into the lens"),
                ("the 50 cm aperture solar telescope installed at Udaipur Solar Observatory designed to capture high-resolution magnetic images of the Sun's chromosphere", "MAST (Multi-Application Solar Telescope)", "DOT", "HCT", "VBT"),
                ("the historic mountain solar observatory established in 1899 in the Palani Hills of Tamil Nadu maintaining an uninterrupted daily solar image archive for over 120 years", "Kodaikanal Solar Observatory (KSO, operated by IIA)", "Udaipur Solar Observatory", "Hanle Observatory", "Nainital Observatory"),
                ("the groundbreaking solar discovery made by John Evershed at Kodaikanal Solar Observatory in January 1909", "Evershed Effect (radial outward gas flow in sunspot penumbrae)", "Discovery of sunspots", "Discovery of solar flares", "Discovery of the solar core"),
                ("the major optical observatory located at Kavalur in the Javadi Hills of Tamil Nadu named after the pioneering Indian astronomer", "Vainu Bappu Observatory (VBO, Kavalur)", "Udaipur Observatory", "Hanle Observatory", "Devasthal Observatory"),
                ("the 2.34-metre optical reflecting telescope at Kavalur which was the largest optical telescope in Asia from 1986 to 2016", "Vainu Bappu Telescope (VBT, 2.34 m)", "Himalayan Chandra Telescope", "Devasthal Telescope", "Girawali Telescope"),
                ("the only Indian astronomer to have discovered a comet (Comet Bappu-Bok-Newkirk in 1949) and who served as President of the International Astronomical Union", "Dr. M.K. Vainu Bappu", "Prof. Govind Swarup", "Prof. Jayant Narlikar", "Dr. Homi Bhabha"),
                ("the stellar spectroscopic discovery co-formulated by Olin Wilson and Vainu Bappu linking the chromospheric luminosity of stars to spectral line widths", "Wilson-Bappu Effect (in Ca II K-line emission)", "Raman Effect", "Doppler Effect", "Zeeman Effect"),
                ("the optical reflecting telescope installed at Mount Abu, Rajasthan at Gurushikhar peak (1,680 m) by PRL dedicated to infrared astronomical observations", "Mount Abu 1.2-metre (and 2.5-metre) Infrared Telescope", "Udaipur Solar Telescope", "ARIES Telescope", "Kavalur Telescope")
            ],
            'tmpls': [
                "Which island solar facility is defined as: {0}?",
                "What thermal aquatic microclimate rationale explains why: {0}?",
                "Which multi-application solar telescope corresponds to: {0}?",
                "Which historic century-old mountain solar observatory represents: {0}?",
                "Which famous solar penumbral hydrodynamic discovery corresponds to: {0}?",
                "Which premier optical facility in Javadi Hills corresponds to: {0}?",
                "Which 2.34-metre historic optical reflector represents: {0}?",
                "Name the renowned comet discoverer and IAU president: {0}.",
                "Which stellar spectroscopic luminosity relationship corresponds to: {0}?",
                "Which infrared mountain facility in Rajasthan represents: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Solar and Optical Facilities Context**\\nThe statement details {item[0]}.\\n**Step 2: Historic Discoveries**\\nUdaipur (MAST on lake island); Kodaikanal (Evershed Effect, 1899); Kavalur (Vainu Bappu Telescope 2.34 m and Wilson-Bappu Effect); Mt. Abu (PRL infrared).\\n**Step 3: Verification**\\nThe matching astronomical facility is {item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 5: Mega-Science Projects: LIGO-India & Thirty Meter Telescope (TMT)
        {
            'data': [
                ("the mega-science advanced gravitational-wave observatory being built at Hingoli, Maharashtra as an exact twin to the two US Advanced LIGO detectors", "LIGO-India (Laser Interferometer Gravitational-Wave Observatory)", "Square Kilometre Array", "Thirty Meter Telescope", "Large Hadron Collider"),
                ("the primary scientific goal of establishing the third Advanced LIGO detector in India alongside the two in Hanford and Livingston (USA)", "To dramatically improve sky localization of gravitational wave sources from neutron star and black hole mergers through long global baselines", "To detect radio broadcasts from alien civilizations", "To measure earthquakes inside Earth's core", "To monitor space debris in LEO"),
                ("the length of each of the two ultra-high vacuum perpendicular arms of the LIGO-India laser interferometer", "\\(4\\text{ kilometres } (4\\text{ km})\\)", "\\(1\\text{ kilometre}\\)", "\\(10\\text{ kilometres}\\)", "\\(500\\text{ metres}\\)"),
                ("the ultra-precise optical principle used in LIGO interferometers to detect spacetime strain distortions smaller than one-thousandth the diameter of a proton", "Laser interferometry using ultra-pure infrared lasers reflected between suspended test mass mirrors in high vacuum", "Radio Doppler radar", "Nuclear magnetic resonance", "Optical refraction through prisms"),
                ("the international mega-science optical telescope consortium in which India is a core partner developing a 30-metre segmented primary mirror telescope", "Thirty Meter Telescope (TMT, planned at Mauna Kea, Hawaii / La Palma)", "Extremely Large Telescope", "James Webb Space Telescope", "Hubble Space Telescope"),
                ("the crucial high-technology hardware components being manufactured by Indian industries for the Thirty Meter Telescope project", "Segment Support Assemblies (SSA), edge sensors, actuators, and primary mirror segment polishing", "Rocket launch boosters", "Satellite solar panels", "Cryogenic fuel tanks"),
                ("the international radio astronomy mega-project comprising thousands of antennas across Australia and South Africa in which India is a founding member", "Square Kilometre Array (SKA)", "LIGO", "TMT", "Event Horizon Telescope"),
                ("the software and telescope management system being developed by Indian computer scientists and NCRA for the Square Kilometre Array (SKA)", "Telescope Manager software system (the 'brain' of SKA)", "Telescope mechanical dishes", "Diesel generators", "Satellite dishes"),
                ("the underground particle physics laboratory proposed in Theni district, Tamil Nadu to detect atmospheric neutrinos", "India-based Neutrino Observatory (INO)", "BARC", "TIFR", "IUCAA"),
                ("why underground caverns beneath massive mountain rock layers (e.g., INO at Pottipuram) are required for neutrino physics detectors", "The mountain rock overhead acts as a massive shield against cosmic ray muons, allowing elusive neutrinos to be detected in quiet conditions", "To protect the laboratory from daylight", "Because neutrinos only travel underground", "To keep detectors cool in winter")
            ],
            'tmpls': [
                "Which flagship gravitational-wave project is defined as: {0}?",
                "What global triangulation advantage explains why: {0}?",
                "What is the physical perpendicular dimension of: {0}?",
                "Which ultra-precise quantum optical measurement principle enables: {0}?",
                "Which 30-metre international segmented optical telescope represents: {0}?",
                "Which precision optomechanical hardware is engineered by India for: {0}?",
                "Which global intercontinental radio array corresponds to: {0}?",
                "Which central control computing architecture is designed for: {0}?",
                "Which proposed underground particle physics project corresponds to: {0}?",
                "What cosmic-ray shielding physics explains why: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Mega-Science Astronomy Context**\\nThe prompt examines {item[0]}.\\n**Step 2: International Collaborations**\\nLIGO-India (4 km arms in Hingoli); TMT (30 m optical segmented mirror); SKA (global radio array with Indian Telescope Manager); INO (underground neutrino detector).\\n**Step 3: Verification**\\nThe matching mega-project is {item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 6: Telescope Optics, Wavelengths & The Electromagnetic Spectrum
        {
            'data': [
                ("a telescope that uses a curved glass lens as its primary objective to bend and focus incident light rays to form an image", "Refracting telescope (Refractor, e.g., Galileo's telescope)", "Reflecting telescope", "Radio telescope", "X-ray telescope"),
                ("a telescope that uses a curved concave mirror as its primary objective to gather and reflect light rays to a focal point", "Reflecting telescope (Reflector, e.g., Newtonian and Cassegrain telescopes)", "Refracting telescope", "Galilean telescope", "Spectroscope"),
                ("why all modern research telescopes of aperture diameter larger than 1 metre are exclusively reflecting telescopes rather than refracting telescopes", "Large mirrors can be supported from behind across their entire back surface and avoid chromatic aberration; heavy glass lenses sag under their own weight and distort images", "Mirrors are made of transparent glass", "Lenses reflect all light away", "Mirrors are lighter than air"),
                ("the optical defect inherent in simple glass lenses where different colors (wavelengths) of white light focus at slightly different focal points", "Chromatic aberration", "Spherical aberration", "Astigmatism", "Diffraction limit"),
                ("the telescope optical configuration where a concave primary mirror reflects light onto a convex secondary mirror that bounces light back through a central hole in the primary mirror", "Cassegrain reflector configuration", "Newtonian reflector", "Galilean refractor", "Gregorian refractor"),
                ("the theoretical limit on the finest angular detail a telescope can resolve governed by the ratio of wavelength to aperture diameter (\\(\\theta \\approx 1.22 \\frac{\\lambda}{D}\\))", "Diffraction limit (Rayleigh's criterion)", "Focal ratio", "Magnification power", "Doppler limit"),
                ("why infrared and X-ray space telescopes (like James Webb, AstroSat) must be launched into space rather than placed on ground mountain peaks", "Earth's atmosphere absorbs infrared, ultraviolet, and X-rays, making the atmosphere opaque to these wavelengths", "Space telescopes do not need electricity", "Ground gravity bends light rays", "Space mirrors never collect dust"),
                ("the specialized radio astronomy technique of linking multiple widely separated radio telescopes electronically to synthesize the resolving power of a single gigantic telescope", "Radio Interferometry (Aperture synthesis, developed by Sir Martin Ryle)", "Optical refraction", "Photometry", "Achromatic coupling"),
                ("the property of a telescope determined by the ratio of the focal length of the objective to the focal length of the eyepiece (\\(M = \\frac{f_o}{f_e}\\))", "Magnifying power (Magnification)", "Light gathering power", "Resolving power", "Aperture ratio"),
                ("the light-gathering power of a telescope is directly proportional to", "The square of the primary objective's diameter (\\(\\text{LGP} \\propto D^2\\))", "The diameter directly (\\(D\\))", "The focal length of the eyepiece", "The length of the telescope tube")
            ],
            'tmpls': [
                "Which lens-based optical instrument class is defined as: {0}?",
                "Which mirror-based optical instrument represents: {0}?",
                "What mechanical support and chromatic rationale explains why: {0}?",
                "Which chromatic optical aberration is defined as: {0}?",
                "Which central hole dual-mirror optical design corresponds to: {0}?",
                "Which fundamental angular resolution limit represents: {0}?",
                "What atmospheric absorption opacity explains why: {0}?",
                "Which multi-antenna synthetic aperture technique represents: {0}?",
                "Which optical parameter formula defines: {0}?",
                "What geometrical proportionality dictates: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Telescope Optics Context**\\nThe statement details {item[0]}.\\n**Step 2: Optical Laws and Performance**\\nReflectors avoid chromatic aberration; \\(\\text{{LGP}} \\propto D^2\\); angular resolution \\(\\theta \\approx 1.22\\frac{{\\lambda}}{{D}}\\); interferometry links baselines to synthesize giant apertures.\\n**Step 3: Verification**\\nThe matching optical concept is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 7: Quantitative Problems in Telescope Resolution, Baselines & Optics
        {
            'data': [
                ("Calculate the light-gathering power comparison between the 3.6-metre Devasthal Optical Telescope (DOT) and a human eye with a pupil diameter of \\(6\\text{ mm } (0.006\\text{ m})\\).", "\\(360,000\\text{ times greater } ((\\frac{3.6}{0.006})^2 = 600^2 = 360,000)\\)", "\\(600\\text{ times}\\)", "\\(36,000\\text{ times}\\)", "\\(1,000,000\\text{ times}\\)"),
                ("Calculate the light-gathering power ratio of the 3.6-metre Devasthal Optical Telescope compared to the 2.0-metre Himalayan Chandra Telescope.", "\\(3.24\\text{ times } ((\\frac{3.6}{2.0})^2 = 1.8^2 = 3.24)\\)", "\\(1.80\\text{ times}\\)", "\\(5.40\\text{ times}\\)", "\\(2.25\\text{ times}\\)"),
                ("An astronomical telescope has an objective of focal length \\(f_o = 150\\text{ cm}\\) and an eyepiece of focal length \\(f_e = 5\\text{ cm}\\). Calculate the magnifying power \\(M\\) of the telescope.", "\\(30\\text{ times } (M = \\frac{150}{5} = 30)\\)", "\\(155\\text{ times}\\)", "\\(750\\text{ times}\\)", "\\(25\\text{ times}\\)"),
                ("A radio interferometer has two antennas separated by a baseline of \\(D = 25\\text{ km } (25,000\\text{ m})\\). When observing at a wavelength of \\(\\lambda = 21\\text{ cm } (0.21\\text{ m})\\), calculate the synthesized angular resolution in radians.", "\\(8.4 \\times 10^{-6}\\text{ radians } (\\frac{0.21}{25000} = 8.4 \\times 10^{-6})\\)", "\\(1.2 \\times 10^{-4}\\text{ rad}\\)", "\\(4.2 \\times 10^{-5}\\text{ rad}\\)", "\\(2.1 \\times 10^{-3}\\text{ rad}\\)"),
                ("Convert the angular resolution of \\(8.4 \\times 10^{-6}\\text{ radians}\\) into arcseconds (taking \\(1\\text{ radian} \\approx 206,265\\text{ arcseconds}\\)).", "\\(1.73\\text{ arcseconds } (8.4 \\times 10^{-6} \\times 206,265 = 1.73\\text{ arcsec})\\)", "\\(0.50\\text{ arcsec}\\)", "\\(5.20\\text{ arcsec}\\)", "\\(10.0\\text{ arcsec}\\)"),
                ("A telescope with an objective diameter of \\(D = 1.22\\text{ metres}\\) observes yellow light of wavelength \\(\\lambda = 600\\text{ nm } (6 \\times 10^{-7}\\text{ m})\\). Calculate the theoretical diffraction limit angle \\(\\theta = 1.22\\frac{\\lambda}{D}\\) in radians.", "\\(6.0 \\times 10^{-7}\\text{ radians}\\)", "\\(1.22 \\times 10^{-6}\\text{ rad}\\)", "\\(3.0 \\times 10^{-7}\\text{ rad}\\)", "\\(6.0 \\times 10^{-5}\\text{ rad}\\)"),
                ("In a 4 km long arm of the LIGO-India interferometer, a laser beam travels back and forth between mirrors 100 times before recombining. What is the effective path length traveled by the laser light?", "\\(400\\text{ km } (4\\text{ km} \\times 100 = 400\\text{ km})\\)", "\\(800\\text{ km}\\)", "\\(40\\text{ km}\\)", "\\(4000\\text{ km}\\)"),
                ("The GMRT has \\(30\\text{ antennas}\\), each with a collecting dish diameter of \\(45\\text{ metres}\\) (area \\(\\approx 1590\\text{ m}^2\\)). Calculate the total collecting area of all 30 dishes combined.", "\\(47,700\\text{ m}^2\\)", "\\(30,000\\text{ m}^2\\)", "\\(15,900\\text{ m}^2\\)", "\\(60,000\\text{ m}^2\\)"),
                ("A liquid mirror telescope dish of diameter \\(4.0\\text{ metres}\\) rotates at \\(8\\text{ rpm}\\) to achieve a focal length of \\(8.0\\text{ metres}\\). If the diameter is doubled to \\(8.0\\text{ metres}\\), by what factor does its light collecting area increase?", "\\(4\\text{ times } (2^2 = 4)\\)", "\\(2\\text{ times}\\)", "\\(8\\text{ times}\\)", "\\(16\\text{ times}\\)"),
                ("If a star has an apparent visual magnitude of \\(m = 1\\) and another star has a magnitude of \\(m = 6\\) (difference \\(\\Delta m = 5\\)), how many times brighter is the first star compared to the second star?", "\\(100\\text{ times brighter } (2.512^5 = 100)\\)", "\\(5\\text{ times}\\)", "\\(10\\text{ times}\\)", "\\(50\\text{ times}\\)")
            ],
            'tmpls': [
                "Calculate telescope light-gathering power relative to human pupil: {0}",
                "Compute comparative aperture light gathering ratio: {0}",
                "Determine telescope angular magnifying power: {0}",
                "Compute synthesized interferometer angular resolution: {0}",
                "Convert radian angular resolution to arcseconds: {0}",
                "Calculate diffraction limit angular threshold: {0}",
                "Compute multi-pass laser optical cavity path length: {0}",
                "Determine total multi-antenna radio collecting area: {0}",
                "Calculate aperture scaling light collection factor: {0}",
                "Evaluate stellar magnitude brightness disparity ratio: {0}"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Formula and Given Quantities**\\nExtract diameters, focal lengths, baselines, wavelengths, or areas from the problem.\\n**Step 2: Arithmetic Evaluation**\\nApply \\(\\text{{LGP}} \\propto D^2\\), \\(M = \\frac{{f_o}}{{f_e}}\\), \\(\\theta = \\frac{{\\lambda}}{{D}}\\), or Pogson's ratio.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)
