import json
import random
import os
from build_cbse8_curi_batch import make_question, get_vaults_and_diffs

random.seed(8831)

def run():
    with open("scripts/cbse8_curi_deficit_manifest.json", "r", encoding="utf-8") as f:
        manifest = json.load(f)

    # -------------------------------------------------------------------------
    # CHAPTER 11 DATA
    # -------------------------------------------------------------------------
    ch11_cases = {
        "CBSE-8-CURI-11-11.1.1": [
            ("The cyclical change in the visible illuminated portion of the Moon as viewed from Earth is termed:", "Phases of the Moon", ["Lunar eclipses", "Solar flares", "Tidal shifts"]),
            ("The moon phase when the Moon is positioned between the Earth and the Sun, and its dark unilluminated hemisphere faces Earth, is called:", "New Moon (Amavasya)", ["Full Moon (Purnima)", "First Quarter", "Waxing Gibbous"]),
            ("The moon phase when the entire illuminated hemisphere of the Moon faces Earth as a complete, dazzling circular disc is:", "Full Moon (Purnima)", ["New Moon", "Crescent Moon", "Waning Crescent"]),
            ("During the waxing fortnight (Shukla Paksha), the visible illuminated portion of the Moon:", "Grows larger night after night from Crescent to Gibbous to Full Moon", ["Shrinks until it disappears", "Changes color from blue to red", "Remains constant in size"])
        ],
        "CBSE-8-CURI-11-11.1.2": [
            ("Does the Moon produce and emit its own visible light like the Sun?", "No, the Moon is a non-luminous celestial body that is visible only because it reflects incident sunlight to our eyes", ["Yes, through nuclear fusion inside its core", "Yes, through radioactive rocks", "Yes, by electrical sparks"]),
            ("Why do we observe different phases of the Moon from Earth throughout the month?", "As the Moon revolves around the Earth, the fraction of its sunlit illuminated half visible from our vantage point changes continuously", ["The Moon changes its physical shape like dough", "Earth's shadow covers the Moon every single night", "Clouds permanently block parts of the Moon"]),
            ("Why do we always see the same side (near side) of the Moon from Earth?", "Synchronous rotation: the Moon's orbital revolution period around Earth exactly equals its axial rotation period (approx. 27.3 days)", ["The Moon does not rotate on its axis at all", "The far side is transparent like glass", "Earth's gravity holds the Moon with steel ropes"]),
            ("The phase when more than half but not the entire illuminated disk of the Moon is visible from Earth is termed:", "Gibbous Moon", ["Crescent Moon", "Quarter Moon", "New Moon"])
        ],
        "CBSE-8-CURI-11-11.1.3": [
            ("The time interval between two consecutive New Moons (a Synodic Lunar Month) is approximately:", "29.5 days (about 29 days, 12 hours, and 44 minutes)", ["Exactly 24 hours", "365.25 days", "15 days exactly"]),
            ("In Indian astronomy, what is a 'Tithi' defined as?", "A lunar day, defined as the time taken by the longitudinal angle between the Moon and the Sun to increase by \\(12^\\circ\\)", ["The exact time from sunrise to sunset", "A complete calendar year", "The orbital period of Mars"]),
            ("A complete lunar month is divided into two distinct fortnights (Pakshas) known in India as:", "Shukla Paksha (bright/waxing fortnight) and Krishna Paksha (dark/waning fortnight)", ["Rabi and Kharif", "Summer and Winter", "Solstice and Equinox"]),
            ("How many Tithis constitute one complete lunar month (Masa) in the Indian calendar?", "30 Tithis (15 in Shukla Paksha ending in Purnima, and 15 in Krishna Paksha ending in Amavasya)", ["12 Tithis", "365 Tithis", "7 Tithis"])
        ],
        "CBSE-8-CURI-11-11.2.1": [
            ("How did ancient human civilizations track time, days, and changing seasons before mechanical clocks were invented?", "By observing periodic celestial motions: Earth's rotation (day/night), Moon's phases (month), and Sun's seasonal path (year)", ["By counting heartbeats continuously", "By listening to bird songs only", "By weighing river sand"]),
            ("Which ancient astronomical timekeeping instrument measures the time of day by the shadow cast by an inclined gnomon on a dial?", "A Sundial (such as the giant Samrat Yantra at Jantar Mantar)", ["A Water Clock (Clepsydra)", "An Hourglass sand timer", "A Seismograph"]),
            ("Who built the magnificent architectural astronomical observatories known as Jantar Mantar in Delhi, Jaipur, Ujjain, Varanasi, and Mathura?", "Maharaja Sawai Jai Singh II of Jaipur (18th century)", ["Emperor Ashoka", "Aryabhata", "Raja Raja Chola"]),
            ("Why do ordinary outdoor sundials read slightly different local solar times across different cities in India?", "Local solar noon occurs at different moments as Earth rotates eastward across different geographical longitudes", ["Sundials only work in winter", "The Moon's gravity bends shadows", "Sundials run on magnetic fields"])
        ],
        "CBSE-8-CURI-11-11.2.2": [
            ("A purely lunar calendar system is based strictly on:", "Twelve consecutive lunar synodic months of 29.5 days each, totaling approximately 354 days per year", ["The orbital revolution of Earth around the Sun (365.25 days)", "The transit of Venus across the Sun", "The rotation of Jupiter"]),
            ("Which international religious calendar is an example of a purely lunar calendar that does not add leap days or leap months?", "The Islamic (Hijri) Calendar", ["The Gregorian Civil Calendar", "The Julian Calendar", "The Saka National Calendar"]),
            ("Because a purely lunar year of 354 days is about 11 days shorter than the solar year (365 days):", "Lunar calendar months and religious festivals drift backwards through the natural solar seasons over a ~33-year cycle", ["The year is permanently locked to harvest season", "Winter and summer occur at the same time", "The Sun stops rising in the East"]),
            ("How many days are in a typical purely lunar year of 12 lunar months?", "Approximately 354 days (\\(12 \\times 29.5 = 354\\))", ["365 days", "366 days", "300 days"])
        ],
        "CBSE-8-CURI-11-11.2.3": [
            ("A solar calendar system is based primarily on:", "The orbital period of the Earth around the Sun (the tropical year of 365.2422 solar days)", ["The phases of the Moon", "The transit of Halley's Comet", "The rotation of Mars"]),
            ("The internationally standard civil calendar used worldwide for business and civil administration is the:", "Gregorian Calendar (introduced by Pope Gregory XIII in 1582)", ["Julian Calendar", "Hijri Calendar", "Mayan Calendar"]),
            ("Why does the Gregorian solar calendar add an extra 'Leap Day' (February 29) every four years?", "To account for the approximately \\(0.25\\) extra day (6 hours) in Earth's orbital period (\\(365.2422\\ \\text{days}\\)) and keep calendar dates aligned with seasons", ["To celebrate ancient Roman emperors", "Because the Earth spins slower in February", "To make all months exactly 30 days"]),
            ("According to the Gregorian leap year rule, century years (like 1700, 1800, 1900, 2000) are leap years ONLY if:", "They are exactly divisible by 400 (e.g., 2000 was a leap year, but 1900 was not)", ["They are divisible by 10", "They end in zero", "They are divisible by 100 only"])
        ],
        "CBSE-8-CURI-11-11.2.4": [
            ("What is a Luni-Solar calendar system (such as the traditional Indian Panchang and Hebrew calendar)?", "A calendar based on lunar months that periodically synchronizes with the solar seasonal year by adding an extra intercalary month", ["A calendar that ignores both Sun and Moon", "A calendar having only 6 months", "A calendar tracking planetary comets"]),
            ("What is the extra intercalary lunar month added roughly every 2.5 to 3 years in the traditional Indian calendar called?", "Adhika Masa (Purushottam Masa or Mala Masa)", ["Chaitra", "Kartik", "Shravan"]),
            ("Why is an intercalary month (Adhika Masa) essential in the Indian Luni-Solar calendar?", "To compensate for the 11-day annual difference between the 354-day lunar year and the 365-day solar year, ensuring harvest festivals occur in their correct seasons", ["To make workers take extra vacation", "Because the Moon pauses in space", "To prevent solar eclipses"]),
            ("Without the periodic addition of Adhika Masa in a luni-solar system:", "Festivals like Holi (spring) and Diwali (autumn) would drift into mid-winter or summer over time", ["The calendar would match the Gregorian dates permanently", "The Sun would rise in the West", "A day would have 30 hours"])
        ],
        "CBSE-8-CURI-11-11.2.5": [
            ("What is the official Indian National Calendar adopted by the Government of India in 1957 alongside the Gregorian calendar?", "The Saka Calendar (Saka Samvat, commencing in 78 CE)", ["The Vikram Samvat", "The Hijri Calendar", "The Julian Calendar"]),
            ("What is the first month of the Indian National (Saka) Calendar?", "Chaitra (commencing on March 22 in a normal year, or March 21 in a leap year)", ["Vaishakha", "Kartika", "Magha"]),
            ("How many days does the Indian National Calendar possess, and how are its month lengths structured?", "365 days (366 in leap year), with Chaitra having 30/31 days followed by 5 months of 31 days and 6 months of 30 days", ["354 days divided into 10 months", "300 days divided into 6 months", "400 days divided into 20 months"]),
            ("Which prominent Indian astrophysicist chaired the Calendar Reform Committee appointed by the Government of India that designed the unified National Calendar?", "Professor Meghnad Saha", ["Homi Bhabha", "Subrahmanyan Chandrasekhar", "C. V. Raman"])
        ],
        "CBSE-8-CURI-11-11.3.1": [
            ("Why are traditional Indian cultural festivals intrinsically connected to celestial astronomical events?", "Ancient Indian agrarian society tied festivals to lunar phases, seasonal solar equinoxes, and crop harvest cycles", ["Festivals were chosen by lottery", "Festivals were dictated by foreign travelers", "Festivals only occur on cloudy days"]),
            ("The colorful spring festival of Holi is celebrated on which celestial lunar day of the Hindu calendar month of Phalguna?", "Purnima (Full Moon night)", ["Amavasya (New Moon night)", "First quarter crescent", "Third quarter"]),
            ("The harvest and solar transition festival of Makar Sankranti (Pongal / Lohri / Bihu) is unique in India because it is based on:", "A fixed solar transit (the entry of the Sun into the zodiac constellation of Makara / Capricorn, usually January 14/15)", ["A lunar New Moon", "A lunar eclipse only", "A fixed Gregorian decree"]),
            ("The Islamic festival of Eid-ul-Fitr is celebrated upon:", "The sighting of the thin waxing crescent Moon (Hilal) marking the end of the fasting month of Ramadan", ["The occurrence of a Full Moon", "The winter solstice", "The solar equinox"])
        ],
        "CBSE-8-CURI-11-11.3.2": [
            ("Which of the following Indian festivals is celebrated on a Full Moon (Purnima) night?", "Raksha Bandhan (Shravana Purnima), Guru Purnima, and Buddha Purnima", ["Diwali", "Maha Shivaratri", "Eid-ul-Fitr"]),
            ("Why is the Full Moon night historically favored for grand cultural gatherings, fairs, and pilgrimages?", "The bright natural illumination provided by the complete lunar disc enabled safe travel and night celebrations before electric lighting existed", ["Full Moon makes the air warm", "Full Moon stops rainfall", "Full Moon removes all diseases"]),
            ("Buddha Purnima commemorates which three pivotal events in the life of Gautama Buddha on the Vaishakha Full Moon?", "His birth, his supreme enlightenment (Nirvana), and his passing away (Parinirvana)", ["His coronation as king only", "His travels to China", "His first agricultural harvest"]),
            ("Guru Nanak Jayanti, celebrating the birth of the first Sikh Guru, is observed annually on the Full Moon day of which month?", "Kartika Purnima", ["Chaitra Purnima", "Magha Purnima", "Ashadha Purnima"])
        ],
        "CBSE-8-CURI-11-11.3.3": [
            ("The festival of lights, Diwali (Deepavali), is celebrated across India on which celestial lunar day of the month of Kartika?", "Amavasya (New Moon night - the darkest night of the month)", ["Purnima (Full Moon night)", "First crescent", "Shukla Ashtami"]),
            ("Why are millions of earthen oil lamps (diyas) and lights illuminated during Diwali?", "To dispel the darkness of the Amavasya night, symbolizing the triumph of light, knowledge, and righteousness over darkness and ignorance", ["To attract summer monsoon clouds", "To cool the autumn atmosphere", "To guide migrating birds"]),
            ("Maha Shivaratri is observed on the 14th night of the Krishna Paksha (waning fortnight) in the month of Magha, just before:", "Amavasya (New Moon)", ["Purnima (Full Moon)", "Makar Sankranti", "Holi"]),
            ("The sighting of the very first delicate sliver of the waxing crescent Moon after Amavasya is culturally auspicious for:", "Eid-ul-Fitr, marking the conclusion of Ramadan, and marking the start of Chaitra Navratri / Gudi Padwa", ["Diwali celebrations", "Holi celebrations", "Winter solstice bonfire"])
        ],
        "CBSE-8-CURI-11-11.3.4": [
            ("What astronomical event occurs on the Summer Solstice (June 21 in the Northern Hemisphere)?", "The Sun reaches its highest northern declination, resulting in the longest day and shortest night of the year", ["Day and night are exactly equal", "The longest night of the year", "The Sun is closest to Earth"]),
            ("What astronomical event occurs on the Winter Solstice (December 21/22 in the Northern Hemisphere)?", "The Sun reaches its southernmost position, giving the shortest day and longest night of the year in the north", ["The longest day of the year", "A total solar eclipse", "The Sun remains at zenith"]),
            ("On the Vernal Equinox (March 20/21) and Autumnal Equinox (September 22/23), what is the relative length of day and night everywhere on Earth?", "Day and night are of approximately equal duration (12 hours of day and 12 hours of night)", ["Day is 18 hours long", "Night is 20 hours long", "The Sun never sets"]),
            ("Harvest festivals celebrated across India in mid-January (Makar Sankranti in Maharashtra/Gujarat, Pongal in Tamil Nadu, Magh Bihu in Assam, Lohri in Punjab) celebrate:", "The solar transit northward (Uttarayana) and the successful reaping of winter agrarian crops", ["The arrival of summer monsoons", "The end of the lunar year", "A total lunar eclipse"])
        ],
        "CBSE-8-CURI-11-11.4.1": [
            ("What is the fundamental difference between a 'Natural Satellite' and an 'Artificial Satellite'?", "A natural satellite is a celestial body (like the Moon) formed naturally in space, while an artificial satellite is a man-made machine launched by rockets to orbit a planet", ["Natural satellites are made of metal", "Artificial satellites have their own gravity like stars", "Artificial satellites orbit the Sun only"]),
            ("How many natural satellites (moons) does planet Earth possess?", "One natural satellite (the Moon)", ["Two moons (Phobos and Deimos)", "Zero moons", "Four moons"]),
            ("What was the world's very first artificial satellite launched into Earth orbit by the Soviet Union on October 4, 1957?", "Sputnik 1", ["Explorer 1", "Aryabhata", "Apollo 11"]),
            ("What keeps an artificial satellite continuously in orbit around the Earth without falling straight down or flying off into space?", "A continuous balance between Earth's inward gravitational pull and the satellite's high forward orbital tangential velocity (free fall around the curve of Earth)", ["Giant rocket thrusters firing continuously 24/7", "Magnetic repulsion from clouds", "Helium gas inside the satellite"])
        ],
        "CBSE-8-CURI-11-11.4.2": [
            ("In which orbit do satellites travel at altitudes of approximately 160 to 2000 km, taking about 90 to 120 minutes to complete one revolution?", "Low Earth Orbit (LEO) (used by the International Space Station and Earth imaging satellites)", ["Geostationary Orbit", "Lunar Orbit", "Lagrange Orbit"]),
            ("A Polar Orbit is an orbit in which an Earth observation satellite travels:", "North-to-South passing over both the North and South Poles, scanning the entire surface as the Earth rotates beneath it", ["Along the equator only", "Around the Moon", "In a fixed geostationary point"]),
            ("What unique property characterizes a Geostationary (Geosynchronous) Orbit located at approximately \\(35{,}786\\ \\text{km}\\) above the Equator?", "Its orbital period matches Earth's 24-hour rotation, making the satellite appear completely stationary over a fixed geographic spot on Earth", ["It orbits Earth every 90 minutes", "It travels backwards from West to East", "It is unaffected by gravity"]),
            ("Why are communication, direct-to-home (DTH) television, and weather monitoring satellites placed in Geostationary Orbit?", "Ground dish antennas on homes and tracking stations can stay pointed permanently at one fixed spot in the sky without motorized tracking", ["Because space is warmer there", "Because signals travel faster in LEO", "Because geostationary satellites do not need solar panels"])
        ],
        "CBSE-8-CURI-11-11.4.3": [
            ("How do meteorological weather satellites (like INSAT and Meteosat) save thousands of human lives every year?", "They track cloud patterns, ocean temperatures, and atmospheric moisture in real-time, providing early warnings for deadly cyclones, floods, and storms", ["They shoot lasers to destroy storm clouds", "They pump cold air onto cities", "They prevent earthquakes"]),
            ("How does the Global Positioning System (GPS / NavIC) determine the precise real-time location of a smartphone user?", "By calculating the exact distance to at least four orbiting navigation satellites using high-precision atomic clock time signals (trilateration)", ["By photographing the user from space", "By reading the user's mind", "By detecting body heat"]),
            ("Satellite remote sensing is critically used in modern agriculture and environmental management to:", "Monitor crop health, estimate agricultural harvest yields, map forest cover, survey groundwater aquifers, and assess drought conditions", ["Spray pesticides from space", "Dig irrigation canals automatically", "Harvest wheat with lasers"]),
            ("Telecommunication satellites facilitate global connectivity by:", "Relaying transcontinental telephone calls, live television broadcasts, maritime navigation signals, and high-speed internet data across oceans", ["Storing all internet data in space clouds", "Filtering out atmospheric radio noise", "Reflecting sunlight onto solar panels at night"])
        ],
        "CBSE-8-CURI-11-11.4.4": [
            ("What was the name of India's first indigenous artificial satellite launched on April 19, 1975, named after the legendary 5th-century Indian astronomer?", "Aryabhata", ["Bhaskara-I", "Rohini", "INSAT-1A"]),
            ("Which premier Indian national space agency founded by Dr. Vikram Sarabhai in 1969 spearheads India's space program?", "Indian Space Research Organisation (ISRO)", ["NASA", "ESA", "Roscosmos"]),
            ("Which historic achievement was accomplished by ISRO's Chandrayaan-3 mission on August 23, 2023?", "India became the first nation in the world to successfully land a spacecraft (Vikram lander and Pragyan rover) near the lunar south pole", ["First human landed on Mars", "First probe launched out of the Solar System", "First telescope placed on the Sun"]),
            ("India's Mars Orbiter Mission (MOM / Mangalyaan), launched by ISRO in 2013, achieved historic world acclaim because:", "India became the first Asian nation to reach Martian orbit and the first nation in the world to succeed on its very first attempt at remarkably low cost", ["It discovered living plants on Mars", "It was manned by four astronauts", "It was launched without a rocket"])
        ]
    }

    # -------------------------------------------------------------------------
    # CHAPTER 12 DATA
    # -------------------------------------------------------------------------
    ch12_cases = {
        "CBSE-8-CURI-12-12.1.1": [
            ("A biological 'habitat' is scientifically defined as:", "The natural physical and biological environment where a specific organism lives, feeds, finds shelter, and reproduces", ["An artificial concrete zoo cage", "A specimen jar in a school laboratory", "The entire continent of Asia"]),
            ("What four essential components must any functional habitat provide for the survival of its resident organisms?", "Food, clean water, adequate shelter/cover, and sufficient space to thrive and reproduce", ["Air conditioning, electricity, television, and furniture", "Only pure mineral rocks and sand", "Only direct sunlight"]),
            ("Why is a polar bear exquisitely adapted to thrive in the icy Arctic tundra habitat but cannot survive in a hot tropical desert?", "Its thick insulating blubber layer, dense white double-fur, and hollow hair fibers trap body heat, causing lethal heatstroke in hot climates", ["Polar bears drink only frozen seawater", "Polar bears have no legs to walk on sand", "Desert air contains no oxygen"]),
            ("If a species' natural habitat is completely destroyed by human urban encroachment, what inevitable consequence faces the species?", "Population collapse and potential extinction due to loss of food, breeding territory, and shelter", ["The species instantly turns into a domestic pet", "The species migrates to the Moon", "The species lives on concrete roads"])
        ],
        "CBSE-8-CURI-12-12.1.2": [
            ("Which of the following is classified as a major Terrestrial (land-based) habitat?", "Dense forests, grasslands, arid deserts, and mountain alpine ecosystems", ["Ocean coral reefs", "Freshwater ponds", "River estuaries"]),
            ("In desert habitats where daytime temperatures soar and water is scarce, how do animals like the camel adapt?", "Fat stored in humps provides metabolic water, long eyelashes block sandstorms, and kidneys produce concentrated urine to minimize water loss", ["Camels sweat ten litres of water hourly", "Camels hibernate underwater in sand", "Camels grow thick fur"]),
            ("Coniferous evergreen trees (like pines, deodars, and firs) in cold mountain habitats possess conical shapes and needle-like leaves to:", "Allow heavy winter snow to slide off branches easily without snapping limbs, and reduce transpiration water loss", ["Absorb maximum wind during storms", "Prevent birds from perching", "Attract mountain goats"]),
            ("Grassland habitats (such as savannahs) are characterized ecologically by:", "Vast expanses of drought-resistant grasses supporting large herds of grazing herbivores and fast apex carnivores", ["Vast deep lakes with zero soil", "Dense canopy trees that block all sunlight", "Permafrost ice cover all year"])
        ],
        "CBSE-8-CURI-12-12.1.3": [
            ("What are the Biotic components of an ecosystem?", "All living organisms including producers (plants), consumers (animals), and decomposers (bacteria and fungi)", ["Air, sunlight, and rainfall", "Soil minerals and temperature", "Water pH and humidity"]),
            ("Why are green plants designated as 'Primary Producers' (autotrophs) in an ecosystem?", "They capture abiotic solar energy and synthesize organic carbohydrates from carbon dioxide and water via photosynthesis", ["They consume other animals for energy", "They decompose dead tree trunks", "They produce mineral rocks"]),
            ("Organisms that obtain energy by feeding on other living organisms are classified ecologically as:", "Consumers (heterotrophs)", ["Producers (autotrophs)", "Abiotic factors", "Inorganic minerals"]),
            ("What vital ecological role is fulfilled by Decomposers (saprophytes like soil bacteria and mushrooms)?", "They break down complex organic matter from dead plants and animal wastes into simple inorganic nutrients recycled back into soil and air", ["They hunt living deer for food", "They block sunlight from reaching the ground", "They eliminate water from the ecosystem"])
        ],
        "CBSE-8-CURI-12-12.1.4": [
            ("How do biotic and abiotic components interact dynamically within a natural ecosystem?", "Biotic organisms continuously exchange matter and energy with their abiotic physical environment (e.g., plants absorb mineral water and solar light)", ["Biotic and abiotic factors never touch each other", "Abiotic factors are created by animal thoughts", "Only animals interact with soil, plants do not"]),
            ("When an earthworm burrows through garden soil, consuming decaying organic matter, how does it alter abiotic soil conditions?", "It aerates the soil, improves moisture infiltration, and enriches soil with nutrient-dense vermicompost casts", ["It compacts soil into solid granite", "It turns soil into acidic vinegar", "It removes all water from soil"]),
            ("How do forest trees influence local abiotic atmospheric weather and climate?", "They absorb carbon dioxide, release oxygen, transpire vast volumes of water vapor creating rainfall clouds, and provide canopy shade", ["They generate toxic chlorine gas", "They stop wind from ever blowing", "They warm the soil to boiling temperatures"]),
            ("If an abiotic factor like annual rainfall drops severely in a region over several consecutive years, what impact is observed on the biotic community?", "Vegetation withers, causing food shortages that decimate herbivore populations, in turn starving apex predators", ["Animal populations multiply ten times", "Plants stop needing water", "All soil minerals turn to gold"])
        ],
        "CBSE-8-CURI-12-12.2.1": [
            ("In ecological hierarchy, an 'organism' is defined as:", "A single, individual living biological entity (such as a single tiger, an oak tree, or an Amoeba)", ["A collection of multiple different species in a forest", "A complete geographical continent", "All non-living rocks in a valley"]),
            ("What fundamental biological property characterizes every living individual organism?", "It maintains cellular homeostasis, metabolizes nutrients, responds to environmental stimuli, grows, and possesses reproductive capacity", ["It is immortal and never dies", "It can live with zero water or food forever", "It has no cell membrane"]),
            ("In a population of 500 chital deer inhabiting a national park, each single deer represents:", "An individual organism", ["An ecosystem", "A biological community", "A biome"]),
            ("Which level of ecological organization serves as the basic fundamental unit upon which natural selection acts directly?", "The individual organism", ["The entire biosphere", "The global biome", "The abiotic soil layer"])
        ],
        "CBSE-8-CURI-12-12.2.2": [
            ("In ecology, a 'population' is formally defined as:", "A group of individual organisms of the SAME species living in a specified geographical area at the same time and capable of interbreeding", ["A mixture of tigers, deer, and trees in a forest", "All animals living across the entire Earth", "The abiotic minerals in a lake"]),
            ("Which of the following represents an ecological population?", "All the Bengal tigers living in the Ranthambore National Park in 2026", ["All trees, birds, insects, and deer in Ranthambore", "The lakes, soil, and rocks of Rajasthan", "A tiger and a lion in a zoo"]),
            ("What two demographic factors directly INCREASE the size of a natural population?", "Births (natality) and Immigration (inflow of individuals from other areas)", ["Deaths (mortality) and Emigration", "Drought and famine", "Predation and disease"]),
            ("What is the maximum population size of a species that a particular natural habitat can sustainably support without environmental degradation?", "Carrying Capacity (\\(K\\))", ["Infinite capacity", "Minimum density", "Extinction threshold"])
        ],
        "CBSE-8-CURI-12-12.2.3": [
            ("A biological 'community' is defined in ecology as:", "An assemblage of interacting populations of DIFFERENT species co-inhabiting a common geographical habitat", ["A group of animals of the same species", "A collection of lifeless stones", "A single isolated organism"]),
            ("Which of the following exemplifies an ecological community?", "All the trees, grasses, deer, monkeys, birds, insects, and soil bacteria living and interacting in the Gir forest", ["All the Asiatic lions in Gir only", "The dry climate and rocky soil of Gujarat", "A herd of cattle in a farm shed"]),
            ("How do different species populations within a biological community interact with one another?", "Through predation, competition for shared resources, mutualistic cooperation, parasitism, and food webs", ["They live in total isolation without awareness of each other", "They all interbreed to form a single hybrid species", "They convert rocks into diamonds"]),
            ("In a pond community, what happens if the population of predatory fish declines sharply due to overfishing?", "The population of small herbivorous fish and tadpoles surges rapidly, in turn overconsuming aquatic algae and depleting resources", ["The pond turns into a desert overnight", "Water evaporates instantly", "Algae multiply uncontrollably"])
        ],
        "CBSE-8-CURI-12-12.2.4": [
            ("An 'ecosystem' encompasses which comprehensive ecological entity?", "The biological community of living organisms (biotic) together with their non-living physical environment (abiotic), functioning as an integrated unit", ["Only the animal populations in a region", "Only the weather and rainfall patterns", "A laboratory microscope slide"]),
            ("What are the two fundamental, defining operational processes of every living ecosystem on Earth?", "Unidirectional energy flow (from Sun through trophic levels) and cyclic biogeochemical nutrient recycling", ["Perpetual motion of water without loss", "Spontaneous creation of new chemical elements", "Complete isolation from solar light"]),
            ("Which of the following is considered a natural ecosystem?", "A natural freshwater lake, a tropical rainforest, and an alpine meadow", ["An artificial concrete parking lot", "A sterile hospital surgery room", "A plastic toy factory"]),
            ("A self-sustaining balanced glass aquarium containing waterweed, small fish, snails, and aquatic bacteria is an example of:", "An artificial, man-made mini-ecosystem", ["A natural wild biome", "A purely abiotic system", "A non-living geological structure"])
        ],
        "CBSE-8-CURI-12-12.2.5": [
            ("Mutualism is a symbiotic biological relationship between two different species in which:", "Both interacting species derive mutual survival and reproductive benefits (+/+ interaction)", ["One species benefits while the other is killed (-/+)", "Both species harm each other (-/-)", "Neither species is affected (0/0)"]),
            ("The mutualistic relationship between flowering plants and pollinating honeybees is mutually beneficial because:", "Honeybees obtain nutritious nectar and pollen for food, while transferring pollen grains between flowers to achieve plant cross-pollination", ["Honeybees eat the plant leaves to death", "Plants trap and digest honeybees", "Neither benefits"]),
            ("A lichen growing on tree bark is a classic partnership of mutualism between which two distinct organisms?", "An alga (or cyanobacterium) providing photosynthetic carbohydrates and a fungus providing water, minerals, and physical shelter", ["A moss and an insect", "A bacterium and a virus", "A protozoan and a worm"]),
            ("Parasitism differs from mutualism because in a parasitic relationship:", "One organism (the parasite) benefits by drawing nutrition at the expense of harming the host (+/- interaction)", ["Both organisms are benefited equally", "The host eats the parasite for calories", "Both organisms die within seconds"])
        ],
        "CBSE-8-CURI-12-12.3.1": [
            ("In an ecosystem, each distinct feeding level in the transfer of food energy is termed a:", "Trophic level", ["Geological stratum", "Taxonomic family", "Thermal zone"]),
            ("Which organisms occupy the First Trophic Level (\\(T_1\\)) in all terrestrial and aquatic food chains?", "Primary producers (green plants, phytoplankton, autotrophs)", ["Primary consumers (herbivores)", "Apex predators (carnivores)", "Decomposers"]),
            ("Herbivorous animals like cows, deer, and grasshoppers that feed directly on green plants occupy which trophic level?", "Second Trophic Level (\\(T_2\\) - Primary Consumers)", ["First Trophic Level", "Third Trophic Level", "Fourth Trophic Level"]),
            ("Apex predators like tigers, lions, and eagles that have no natural predators in their ecosystem occupy the:", "Top Trophic Level (Tertiary / Quaternary Consumers)", ["First Trophic Level", "Second Trophic Level", "Producer Level"])
        ],
        "CBSE-8-CURI-12-12.3.2": [
            ("A Food Chain is defined in ecology as:", "A linear sequential pathway depicting who eats whom, tracing the transfer of food energy from producers through successive consumers", ["A circular ring of plants only", "A list of endangered animals in a zoo", "A recipe book for cooking"]),
            ("Which sequence correctly illustrates a typical terrestrial grassland food chain?", "\\(\\text{Grass (Producer)} \\rightarrow \\text{Grasshopper (Primary Consumer)} \\rightarrow \\text{Frog} \\rightarrow \\text{Snake} \\rightarrow \\text{Eagle (Apex)}\\)", ["\\(\\text{Eagle} \\rightarrow \\text{Snake} \\rightarrow \\text{Frog} \\rightarrow \\text{Grass}\\)", "\\(\\text{Grasshopper} \\rightarrow \\text{Grass} \\rightarrow \\text{Eagle} \\rightarrow \\text{Snake}\\)", "\\(\\text{Frog} \\rightarrow \\text{Grasshopper} \\rightarrow \\text{Eagle} \\rightarrow \\text{Grass}\\)"]),
            ("What is a 'Food Web' in a natural ecosystem, and why is it ecologically realistic compared to an isolated food chain?", "A complex network of interconnected, overlapping food chains reflecting that animals feed on multiple diverse food sources", ["A single straight food line with no branches", "A spiderweb spun to catch flies only", "A human fishing net in the ocean"]),
            ("Why does a complex, highly interconnected food web impart greater ecological resilience and stability to an ecosystem?", "If one prey species population declines, predators can switch to alternative prey species without collapsing the entire community", ["It makes all animals vegetarians", "It eliminates the need for solar energy", "It stops animal deaths permanently"])
        ],
        "CBSE-8-CURI-12-12.3.3": [
            ("What is an 'ecological trophic cascade' in an ecosystem?", "A powerful indirect interaction where changes in the population of an apex predator trigger cascading structural shifts down across lower trophic levels", ["A waterfall flowing into a river", "A sudden heavy rainstorm", "A seasonal migration of birds"]),
            ("When gray wolves (apex predators) were reintroduced into Yellowstone National Park, what dramatic cascade effect was observed?", "Wolves reduced overgrazing by elk, allowing willow trees to regenerate along riverbanks, stabilizing river channels and bringing back beavers and songbirds", ["Wolves destroyed all forest trees", "Wolves evaporated river water", "Wolves caused all birds to die"]),
            ("A 'Keystone Species' in ecology is defined as a species that:", "Has a disproportionately large, indispensable impact on the structure, diversity, and balance of its ecosystem relative to its abundance", ["Has the largest physical body weight", "Is the most numerous species by count", "Lives exclusively in water"]),
            ("If an apex keystone predator (like the Bengal Tiger in Indian forests) is completely eradicated by poaching, what happens?", "Unchecked herbivore populations overgraze forest understory vegetation, causing catastrophic soil erosion, biodiversity loss, and habitat collapse", ["The forest becomes twice as green", "Rainfall doubles immediately", "All rivers flow faster"])
        ],
        "CBSE-8-CURI-12-12.3.4": [
            ("According to Raymond Lindeman's 10 Percent Law of ecological energy transfer, approximately how much energy is transferred from one trophic level to the next?", "Only about 10% of the energy is transferred to the next higher level; roughly 90% is lost as metabolic heat, respiration, and excretion", ["100% of the energy is transferred", "50% is transferred", "90% is transferred"]),
            ("If green plants in a forest ecosystem capture \\(10{,}000\\ \\text{Joules}\\) of solar energy into food, how much energy is available to secondary consumers (carnivores)?", "\\(100\\ \\text{Joules}\\) (Plants: 10,000 J -> Herbivores: 1,000 J -> Carnivores: 100 J)", ["\\(5{,}000\\ \\text{Joules}\\)", "\\(1{,}000\\ \\text{Joules}\\)", "\\(10\\ \\text{Joules}\\)"]),
            ("Why are food chains in nature typically limited to only 3, 4, or at most 5 trophic levels?", "Energy diminishes drastically at each successive trophic transfer (90% loss), leaving insufficient energy to support a viable population of higher consumers", ["Animals run out of space", "Carnivores refuse to eat higher animals", "The Sun stops providing light"]),
            ("How does the movement of ENERGY through an ecosystem differ fundamentally from the movement of NUTRIENTS (matter)?", "Energy flows unidirectionally (in one direction from Sun to heat loss) and cannot be recycled, whereas nutrients cycle continuously in closed biogeochemical loops", ["Energy cycles in circles while nutrients are lost to space", "Both energy and nutrients cycle infinitely", "Neither energy nor nutrients move"])
        ],
        "CBSE-8-CURI-12-12.4.1": [
            ("What is 'Biodiversity' (biological diversity) defined as in ecological science?", "The immense variety and variability of all life forms on Earth, encompassing genetic diversity, species diversity, and ecosystem diversity", ["The total number of trees in an orchard", "The weight of all animals in a zoo", "The amount of water in an ocean"]),
            ("Why is rich biodiversity vital for human survival and economic prosperity?", "Provides essential ecosystem services: oxygen production, climate regulation, freshwater purification, crop pollination, medicinal compounds, and soil fertility", ["Biodiversity makes computers faster", "Biodiversity replaces the need for farming", "Biodiversity stops volcanoes"]),
            ("A biodiverse ecosystem with thousands of interacting species is much more stable and resilient against diseases and climatic extremes because:", "High species richness provides functional redundancy; if one species suffers, other species can maintain vital ecosystem processes", ["It contains no predators", "All species have identical DNA", "It prevents winter frost"]),
            ("What percentage of modern life-saving prescription medicines are derived directly or indirectly from biochemical compounds found in wild plants, fungi, and microbes?", "Approximately 25% to 50% of all pharmaceuticals", ["Zero percent", "Only 0.01%", "100% of all metals"])
        ],
        "CBSE-8-CURI-12-12.4.2": [
            ("What is currently recognized by ecologists as the single greatest global driver of wildlife species extinction?", "Habitat destruction, fragmentation, and degradation caused by agricultural expansion, logging, mining, and urban infrastructure", ["Natural solar flares", "Volcanic eruptions", "Hunting by wild carnivores"]),
            ("How does 'habitat fragmentation' (e.g., cutting a highway or railway line through a dense forest) severely harm wildlife populations?", "Divides continuous populations into small isolated breeding groups, blocks natural migratory corridors, and increases roadkill mortality", ["Allows animals to travel on trains", "Creates new water rivers", "Makes animals run faster"]),
            ("The introduction of aggressive non-native alien invasive species (like Lantana camara weed or African catfish) threatens native ecosystems by:", "Outcompeting, displacing, and preying upon native species, and disrupting balanced indigenous food webs", ["Enriching local wildlife diversity", "Curing all plant diseases", "Increasing freshwater levels"]),
            ("Poaching and unregulated illegal wildlife trade (e.g., tiger skins, elephant ivory, rhino horns) push keystone species towards:", "Rapid demographic collapse and severe risk of global extinction in the wild", ["Domestic breeding in households", "Increased longevity", "Superhuman strength"])
        ],
        "CBSE-8-CURI-12-12.4.3": [
            ("What is the IUCN Red List of Threatened Species internationally established to do?", "Assess and document the global conservation status and extinction risk of thousands of biological plant and animal species worldwide", ["List dangerous animals to be hunted", "List the prices of timber in markets", "Record animal weights in zoos"]),
            ("A species facing an extremely high risk of extinction in the wild in the immediate future is categorized on the IUCN Red List as:", "Critically Endangered (CR)", ["Least Concern (LC)", "Extinct in prehistoric times", "Domesticated"]),
            ("Which iconic Indian bird species, inhabiting dry open grasslands of Rajasthan and Gujarat, is currently on the brink of extinction due to powerline collisions?", "The Great Indian Bustard (Godawan)", ["The House Sparrow", "The Common Pigeon", "The Indian Peafowl"]),
            ("When the very last living individual of a biological species dies anywhere on Earth, the species is classified as:", "Extinct (e.g., Dodo, Passenger Pigeon, Tasmanian Tiger)", ["Endangered", "Vulnerable", "Threatened"])
        ],
        "CBSE-8-CURI-12-12.4.4": [
            ("In-situ conservation is the strategy of conserving biodiversity by:", "Protecting endangered species within their own natural wild habitats (e.g., National Parks, Wildlife Sanctuaries, and Biosphere Reserves)", ["Keeping animals in urban zoological parks", "Storing frozen seeds in botanical seed banks", "Breeding animals in university laboratories"]),
            ("Ex-situ conservation is the strategy of conserving biodiversity by:", "Protecting and breeding threatened species outside their natural habitats in controlled artificial facilities (e.g., Zoos, Botanical Gardens, Seed Banks, Gene Banks)", ["Leaving animals completely unprotected in forests", "Hunting animals for sports", "Farming crops in villages"]),
            ("Which famous Indian National Park in Assam is globally renowned as the premier sanctuary protecting the world's largest population of the One-Horned Rhinoceros?", "Kaziranga National Park", ["Jim Corbett National Park", "Sundarbans National Park", "Kanha National Park"]),
            ("Sundarbans Biosphere Reserve in West Bengal is unique because it protects the world's largest contiguous mangrove ecosystem and the specialized habitat of:", "The Royal Bengal Tiger", ["The Asiatic Lion", "The Snow Leopard", "The Kashmiri Hangul Stag"])
        ],
        "CBSE-8-CURI-12-12.4.5": [
            ("What are 'Sacred Groves' (such as Deorais in Maharashtra, Orans in Rajasthan, and Kavu in Kerala) in Indian cultural heritage?", "Pristine forest patches communally protected for centuries by indigenous rural and tribal communities through spiritual reverence and religious taboos", ["Commercial timber harvesting zones", "Government chemical factory lands", "Private sports grounds"]),
            ("Sacred Groves act as invaluable biodiversity sanctuaries in modern times because they:", "Preserve rare, relict medicinal herbs, endemic plants, and pristine natural water springs that have vanished from surrounding cleared lands", ["Produce synthetic plastics", "Are used for cattle grazing", "Are paved with concrete roads"]),
            ("The historic Bishnoi community of Rajasthan is renowned across the world for which legendary conservation sacrifice in 1730?", "Amrita Devi and 362 Bishnoi villagers sacrificing their lives to protect sacred Khejri trees from being felled by royal woodcutters (Chipko movement precursor)", ["Building the largest palace in Jaipur", "Hunting wild animals for the king", "Digging copper mines"]),
            ("What environmental philosophy underpins traditional Indian ecological heritage across centuries?", "Living in harmonious coexistence with nature, recognizing that all living beings possess sacred value and must be treated with compassion and restraint", ["Conquering and exploiting nature without limits", "Consuming all resources before neighbors do", "Destroying forests for concrete cities"])
        ]
    }

    # -------------------------------------------------------------------------
    # CHAPTER 13 DATA
    # -------------------------------------------------------------------------
    ch13_cases = {
        "CBSE-8-CURI-13-13.1.1": [
            ("Planet Earth is uniquely distinguished among all known celestial bodies in the universe because:", "It is currently the only planet confirmed to harbor, support, and sustain complex biological life", ["It is the largest planet in the Solar System", "It is composed entirely of pure gold", "It is the closest planet to the Sun"]),
            ("Which fundamental life-sustaining substance exists abundantly in liquid form on the surface of Earth across oceans, lakes, and rivers?", "Liquid Water (\\(\\text{H}_2\\text{O}\\))", ["Liquid Methane", "Liquid Nitrogen", "Liquid Sulfuric Acid"]),
            ("What percentage of the Earth's surface is covered by liquid water oceans and seas?", "Approximately 71% (giving Earth its characteristic 'Blue Planet' appearance from space)", ["Approximately 10%", "Exactly 50%", "Over 99%"]),
            ("Earth's life-supporting global ecological envelope encompassing the lower atmosphere, hydrosphere, and upper lithosphere is termed the:", "Biosphere", ["Stratosphere", "Mesosphere", "Core"])
        ],
        "CBSE-8-CURI-13-13.1.2": [
            ("The 'Habitable Zone' (often referred to as the 'Goldilocks Zone') around a star is defined in astrophysics as:", "The orbital region around a star where temperatures are 'just right'—neither too hot nor too cold—for liquid water to exist on a planetary surface", ["The region where stars explode as supernovas", "The zone inside a black hole", "The center of a burning star"]),
            ("What would happen to Earth's oceans if our planet were situated significantly closer to the Sun (like Venus at \\(0.7\\ \\text{AU}\\))?", "Extreme solar radiation would boil the oceans away, triggering a runaway greenhouse catastrophe and an uninhabitable furnace", ["Oceans would freeze into solid ice", "Water would turn into pure oil", "Oceans would double in size"]),
            ("What would happen to Earth's water if our planet were situated much farther from the Sun (like Mars at \\(1.5\\ \\text{AU}\\))?", "Surface temperatures would plummet, freezing all surface water into permanent, solid ice glaciers", ["Water would boil violently", "The oceans would evaporate into space", "Water would turn into acid"]),
            ("Earth's nearly circular orbit around the Sun at an average distance of \\(1\\ \\text{AU}\\) (approx. \\(150\\ \\text{million km}\\)) ensures:", "A relatively stable, moderate climate without extreme wild seasonal temperature oscillations", ["Constant freezing winter all year", "Absence of any day or night", "Permanent total eclipses"])
        ],
        "CBSE-8-CURI-13-13.1.3": [
            ("What is the average global mean surface temperature of planet Earth that makes liquid water and biological metabolism possible?", "Approximately \\(+15^\\circ\\text{C}\\) (around \\(288\\ \\text{K}\\))", ["\\(-50^\\circ\\text{C}\\)", "\\(+100^\\circ\\text{C}\\)", "\\(+450^\\circ\\text{C}\\)"]),
            ("Without the natural greenhouse effect produced by atmospheric water vapor, \\(\\text{CO}_2\\), and methane, what would Earth's average surface temperature be?", "Approximately \\(-18^\\circ\\text{C}\\) (a frozen, lifeless planetary ice-ball)", ["\\(+500^\\circ\\text{C}\\)", "\\(0^\\circ\\text{C}\\) exactly", "Absolute zero (\\(-273^\\circ\\text{C}\\))"]),
            ("Why is the presence of liquid water within the \\(0^\\circ\\text{C}\\ \\text{to}\\ 100^\\circ\\text{C}\\) range strictly indispensable for organic life?", "Water serves as the universal biochemical reaction solvent, transports nutrients and wastes in blood/sap, and maintains cellular structural turgidity", ["Water burns into cellular heat", "Water has zero mass", "Water is made of gold atoms"]),
            ("Earth's axial tilt of approximately \\(23.5^\\circ\\) relative to its orbital plane is responsible for producing:", "The annual cycle of four distinct seasons (Spring, Summer, Autumn, Winter) distributing solar warmth across latitudes", ["The daily cycle of sunrise and sunset", "Earth's magnetic field", "Tectonic continental drift"])
        ],
        "CBSE-8-CURI-13-13.1.4": [
            ("Earth's outermost solid rocky shell that provides the physical foundation for terrestrial life, agriculture, and minerals is the:", "Crust (Lithosphere)", ["Mantle", "Outer molten core", "Inner solid core"]),
            ("Fertile agricultural soil, which sustains all global food crop production, is formed by which geological process over centuries?", "The slow physical, chemical, and biological weathering of crustal rocks mixed with decaying organic humus", ["Fast volcanic ash freezing in water", "Direct condensation of atmospheric oxygen", "Nuclear decay of diamonds"]),
            ("Earth's dynamic internal tectonic heat drives plate tectonics, which performs the vital geological role of:", "Recycling carbon and minerals through volcanic outgassing and subduction, renewing the crust and maintaining long-term climate stability", ["Stopping the Earth from rotating", "Cooling the oceans into solid ice", "Freezing all underground water"]),
            ("Which light chemical elements make up the vast majority of continental crust rocks (forming granite and silica minerals)?", "Silicon and Aluminium (Sial)", ["Iron and Nickel (Nife)", "Hydrogen and Helium", "Uranium and Plutonium"])
        ],
        "CBSE-8-CURI-13-13.2.1": [
            ("Why is planet Mercury completely incapable of sustaining organic life?", "It has virtually no atmosphere to retain heat or block solar rays, causing wild temperature swings from \\(+430^\\circ\\text{C}\\) by day to \\(-180^\\circ\\text{C}\\) by night", ["Mercury is covered by deep liquid oceans", "Mercury is made entirely of ice", "Mercury is too far from the Sun"]),
            ("Why is Venus often described as an 'infernal twin' of Earth?", "It has a super-dense \\(\\text{CO}_2\\) atmosphere (92 bars pressure) with runaway greenhouse heating scorching the surface at \\(465^\\circ\\text{C}\\) with sulfuric acid clouds", ["It is freezing cold at \\(-200^\\circ\\text{C}\\)", "It has blue freshwater oceans", "It has zero gravity"]),
            ("Why is planet Mars currently hostile and sterile for unprotected human life?", "It has an extremely thin \\(\\text{CO}_2\\) atmosphere (less than 1% of Earth's), sub-zero average temperature (\\(-60^\\circ\\text{C}\\)), no liquid surface water, and deadly cosmic radiation", ["Mars has a surface gravity ten times Earth's", "Mars is too hot at \\(800^\\circ\\text{C}\\)", "Mars is made of liquid gas"]),
            ("Gas giant planets (Jupiter, Saturn, Uranus, Neptune) cannot support terrestrial life because they:", "Lack a solid physical surface to walk on, possess crushing atmospheric pressures of millions of atmospheres, and violent turbulent storms", ["Are too close to the Sun and boiling", "Are made of pure oxygen gas", "Have zero gravity"])
        ],
        "CBSE-8-CURI-13-13.2.2": [
            ("What catastrophic planetary atmospheric phenomenon transformed Venus from a potentially habitable world into an arid furnace?", "A runaway greenhouse effect where evaporating oceans saturated the atmosphere with water vapor, trapping heat until all water was lost to space", ["A sudden meteor that stripped its crust", "The Sun freezing its atmosphere", "Extensive plant growth consuming all carbon"]),
            ("Why did Mars lose most of its ancient atmosphere and surface water over the past 3.5 billion years?", "Mars is small and cooled rapidly; its internal core dynamo solidified, shutting down its global magnetic field and allowing the solar wind to strip its atmosphere", ["Martian volcanoes swallowed all air", "Mars drifted too close to Jupiter", "A giant black hole passed through Mars"]),
            ("Unlike Venus and Mars, Earth has successfully maintained stable, life-supporting surface conditions over billions of years because of:", "Active plate tectonics, a protective global magnetic field, an optimal distance from the Sun, and self-regulating biogeochemical carbon cycles", ["Complete absence of an atmosphere", "Earth having no volcanoes or earthquakes", "Earth never rotating on its axis"]),
            ("The runaway greenhouse effect on Venus serves as an urgent planetary warning to humanity that:", "Excessive accumulation of greenhouse gases in an atmosphere can destabilize planetary climate beyond tipping points of recovery", ["Carbon dioxide is completely harmless", "Planetary climates never change", "Oceans cannot evaporate"])
        ],
        "CBSE-8-CURI-13-13.2.3": [
            ("Which unique combination of physical conditions allows Earth to support complex multicellular animal and plant life?", "Abundant liquid water, an oxygen-rich atmosphere (21%), moderate climate, protective ozone and magnetic shields, and rich soil minerals", ["Zero atmospheric pressure and pure helium gas", "Extreme sub-zero polar temperatures worldwide", "Dense clouds of sulfuric acid vapor"]),
            ("Why was the biological Great Oxidation Event (triggered by photosynthetic cyanobacteria ~2.4 billion years ago) revolutionary for life on Earth?", "It filled the atmosphere with free molecular oxygen (\\(\\text{O}_2\\)), enabling highly efficient aerobic cellular respiration and forming the protective ozone layer", ["It caused all oceans to freeze solid", "It eliminated all sunlight from reaching the ground", "It created the Moon"]),
            ("What special property of planet Earth's Moon stabilizes our planetary climate and seasons over astronomical timescales?", "The Moon's large mass exerts gravitational tidal torque that stabilizes Earth's \\(23.5^\\circ\\) axial tilt, preventing chaotic climatic wobbles", ["The Moon shines bright yellow light for photosynthesis", "The Moon's gravity warms the Earth's core", "The Moon blocks all solar flares"]),
            ("How do living organisms themselves actively modify and regulate the Earth's environment to keep it habitable (the Gaia Hypothesis concept)?", "Plants regulate atmospheric \\(\\text{CO}_2\\) and oxygen levels, while marine organisms lock excess carbon into limestone sea shells and ocean sediments", ["Animals build concrete cities", "Microbes burn sulfur in space", "Trees absorb all ocean water"])
        ],
        "CBSE-8-CURI-13-13.3.1": [
            ("Planet Earth is scientifically modeled as an integrated global system comprising four interconnected spheres called:", "Geosphere (Lithosphere), Hydrosphere, Atmosphere, and Biosphere", ["Crust, Mantle, Core, and Magma only", "Troposphere, Stratosphere, Mesosphere, and Thermosphere", "Solid, Liquid, Gas, and Plasma"]),
            ("The Hydrosphere encompasses:", "All the water on Earth in liquid, solid, and gaseous forms across oceans, rivers, lakes, glaciers, groundwater, and clouds", ["Only the deep underground lava rocks", "Only the nitrogen gas in the sky", "Only the living animals in forests"]),
            ("The Atmosphere is the blanket of gases surrounding Earth, primarily composed of which two dominant gases?", "Nitrogen (about 78%) and Oxygen (about 21%)", ["Carbon dioxide (90%) and Methane (10%)", "Hydrogen (75%) and Helium (25%)", "Pure Ozone (100%)"]),
            ("How do the Geosphere, Hydrosphere, and Atmosphere intersect to create the Biosphere?", "Living organisms thrive precisely at the boundary interface where solid land, liquid water, and breathable air meet and interact", ["The Biosphere exists only deep inside the molten mantle", "The Biosphere is outside the atmosphere in space", "The spheres never touch each other"])
        ],
        "CBSE-8-CURI-13-13.3.2": [
            ("What is a 'Biogeochemical Cycle' in Earth system science?", "A natural cyclical pathway by which essential chemical elements (like water, carbon, nitrogen, and phosphorus) circulate between living biotic and non-living abiotic spheres", ["A mechanical bicycle powered by biofuel", "A volcanic explosion cycle", "A method of mining metal ores"]),
            ("In the global Hydrological (Water) Cycle, water moves continuously between the Earth's surface and the atmosphere through which sequential physical processes?", "Evaporation/Transpiration \\(\\rightarrow\\) Condensation into clouds \\(\\rightarrow\\) Precipitation (rain/snow) \\(\\rightarrow\\) Surface runoff and groundwater infiltration", ["Boiling \\(\\rightarrow\\) Freezing \\(\\rightarrow\\) Melting \\(\\rightarrow\\) Sublimation", "Filtration \\(\\rightarrow\\) Distillation \\(\\rightarrow\\) Crystallization", "Photosynthesis \\(\\rightarrow\\) Respiration \\(\\rightarrow\\) Fermentation"]),
            ("In the global Carbon Cycle, how is carbon dioxide removed from the atmosphere, and how is it returned back to the air?", "Removed by plant photosynthesis and ocean dissolution; returned by plant/animal cellular respiration, microbial decomposition, and combustion of fuels", ["Removed by breathing; returned by rain", "Removed by volcanic eruptions; returned by ice", "Carbon never changes form"]),
            ("The global Nitrogen Cycle is vital for all living organisms because nitrogen is an essential building block of:", "Proteins, nucleic acids (DNA and RNA), and amino acids", ["Pure table sugar", "Calcium bone mineral only", "Water molecules"])
        ],
        "CBSE-8-CURI-13-13.3.3": [
            ("In which layer of the Earth's atmosphere is the vital life-protecting Ozone Layer (\\(\\text{O}_3\\)) concentrated?", "The Stratosphere (between approximately 15 and 35 km altitude)", ["The Troposphere", "The Mesosphere", "The Thermosphere"]),
            ("What crucial ecological shielding function is performed by the stratospheric Ozone Layer?", "It absorbs over 98% of the Sun's harmful high-energy Ultraviolet-B and Ultraviolet-C (UV) radiation, protecting life on Earth", ["It blocks visible sunlight from reaching ground", "It keeps atmospheric oxygen from escaping to space", "It reflects radio signals for WiFi"]),
            ("What dangerous biological consequences occur when humans and animals are exposed to excessive, unshielded ultraviolet (UV) radiation?", "Skin cancers (melanoma), painful cataracts and corneal damage in eyes, sunburn, and severe suppression of the immune system", ["Increased muscular stamina", "Rapid growth of hair", "Complete immunity to diseases"]),
            ("Which industrial synthetic chemicals, used in old refrigerators and aerosol spray cans, caused severe catalytic destruction of the ozone layer ('Ozone Hole')?", "Chlorofluorocarbons (CFCs) and halons (regulated globally by the historic 1987 Montreal Protocol)", ["Carbon dioxide and water vapor", "Nitrogen and argon gases", "Methane and propane"])
        ],
        "CBSE-8-CURI-13-13.3.4": [
            ("What generates Earth's powerful global geomagnetic field (magnetosphere)?", "Convection currents and swirling eddies of molten iron and nickel in Earth's liquid outer core behaving as a geodynamo", ["Permanent solid iron magnets in mountains", "Electric current in overhead lightning", "The rotation of the Moon around Earth"]),
            ("What vital shielding role does Earth's Magnetosphere perform to safeguard our planet's atmosphere and life?", "It deflects the deadly stream of high-energy charged particles (Solar Wind and galactic cosmic rays) streaming from the Sun away from Earth", ["It stops rain from falling too fast", "It prevents ocean waves from rising", "It cools the air at the equator"]),
            ("What happens to charged solar wind particles that get trapped and channeled along magnetic field lines into the upper polar atmosphere?", "They collide with atmospheric oxygen and nitrogen atoms, exciting them to produce spectacular dancing light displays called Auroras (Northern and Southern Lights)", ["They create volcanic eruptions on ice", "They freeze polar bears", "They destroy the Earth's crust"]),
            ("If Earth's magnetic field were to vanish permanently, what would happen over geological time?", "The relentless solar wind would strip away our atmosphere (just as occurred on Mars), exposing surface life to lethal cosmic radiation", ["Earth would drift out of the Solar System", "The oceans would turn into gold", "Earth would become two times larger"])
        ],
        "CBSE-8-CURI-13-13.4.1": [
            ("What is the primary anthropogenic (human-caused) driver of modern Global Warming and Climate Change?", "The excessive burning of fossil fuels (coal, petroleum, natural gas) and massive deforestation releasing billions of tons of \\(\\text{CO}_2\\) and greenhouse gases", ["Solar eclipses occurring too frequently", "Natural respiration of wild forest animals", "Volcanic eruptions in oceans"]),
            ("How does an increased concentration of greenhouse gases in the atmosphere cause global warming?", "They trap outgoing infrared thermal radiation emitted by Earth's surface, preventing heat from escaping into outer space and warming the climate", ["They generate their own nuclear heat", "They reflect visible light back to the Sun", "They destroy all cold air molecules"]),
            ("Which observable global environmental crisis is a direct consequence of rising global average temperatures?", "Accelerated melting of polar ice caps and glaciers, leading to global sea level rise, submergence of coastal islands, and extreme weather events", ["Global cooling into a permanent ice age", "Disappearance of all deserts", "Reduction in cyclonic storm intensity"]),
            ("Ocean Acidification, which threatens coral reefs and marine shellfish, is directly caused by:", "The absorption of excess atmospheric carbon dioxide into ocean waters, forming carbonic acid (\\(\\text{H}_2\\text{CO}_3\\)) and lowering seawater pH", ["Dumping plastic wrappers in rivers", "Oil spills on beaches only", "Overfishing of sharks"])
        ],
        "CBSE-8-CURI-13-13.4.2": [
            ("What is 'Sustainable Resource Stewardship' defined as in environmental science?", "Using natural resources responsibly to meet the needs of the present generation without compromising the ability of future generations to meet their own needs", ["Consuming all available resources as quickly as possible", "Banning the use of all energy and water permanently", "Selling all natural resources abroad"]),
            ("Which of the following is classified as an infinitely Renewable, clean energy resource?", "Solar energy, wind energy, hydroelectric power, and geothermal energy", ["Coal", "Crude petroleum oil", "Natural gas"]),
            ("Why is transition from fossil fuels to renewable energy (like solar and wind power) imperative for human civilization?", "Fossil fuel reserves are finite and their combustion drives dangerous climate change, whereas solar and wind energy are inexhaustible and produce zero emissions", ["Renewable energy is made of pure coal", "Solar panels work only underground", "Fossil fuels will turn into diamonds"]),
            ("Rainwater Harvesting in homes and communities promotes sustainable water stewardship by:", "Collecting and storing rooftop rainwater or channeling it into underground aquifers to recharge groundwater tables and prevent water scarcity", ["Draining all groundwater into oceans", "Boiling rainwater into steam for heat", "Evaporating rainwater quickly"])
        ],
        "CBSE-8-CURI-13-13.4.3": [
            ("What does the 'Circular Economy' model advocate compared to the traditional linear 'Take-Make-Dispose' industrial model?", "Designing products to minimize waste, keeping materials and resources in use continuously through remanufacturing, refurbishment, and recycling", ["Throwing away goods after a single use into landfills", "Incinerating all household waste in open streets", "Manufacturing goods that break within one week"]),
            ("What do the '5 R's' of modern sustainable waste management stand for?", "Refuse, Reduce, Reuse, Repurpose, and Recycle", ["React, Refuse, Remove, Reheat, and Repeat", "Recover, Reheat, Reshape, Replace, and Refine", "Record, Report, Review, Repair, and Reject"]),
            ("Under the 5 R framework, what is the most powerful and effective initial step in curbing plastic pollution?", "REFUSE single-use disposable plastics (like plastic straws, disposable bags, and styrofoam cups) at the point of purchase", ["Recycle dirty plastic wrappers at home", "Bury plastics in farmland", "Burn plastic bottles in gardens"]),
            ("Separating household municipal waste at the source into 'Wet Waste' (biodegradable food scraps) and 'Dry Waste' (paper, glass, metal, plastic) enables:", "Converting wet waste into organic compost fertilizer and directing dry materials to dedicated recycling facilities", ["Dumping all waste together into lakes", "Burning wet waste in open barrels", "Mixing waste into drinking water"])
        ],
        "CBSE-8-CURI-13-13.4.4": [
            ("Which simple individual daily action significantly reduces an individual's carbon footprint and conserves electricity?", "Switching off lights, fans, and appliances when leaving a room, and using energy-efficient LED bulbs and star-rated appliances", ["Leaving air conditioners running with windows open", "Using incandescent bulbs instead of LEDs", "Leaving television sets on standby all night"]),
            ("How does opting to walk, ride a bicycle, or use public transit (metro/buses) instead of private motorcars benefit city environments?", "Reduces urban air pollution emissions, lowers fossil fuel consumption, and decreases road traffic congestion", ["Increases greenhouse gas emissions", "Consumes extra petroleum fuels", "Causes city traffic jams"]),
            ("Community tree-planting drives (Van Mahotsav) contribute to planetary healing by:", "Sequestering carbon dioxide, restoring urban green cover, providing bird habitats, preventing soil erosion, and cooling ambient microclimates", ["Consuming all groundwater permanently", "Emitting carbon dioxide in daylight", "Attracting desert locusts"]),
            ("Why is collective civic awareness and youth leadership crucial for global environmental conservation?", "Informed citizens drive sustainable public policies, hold industries accountable to environmental standards, and adopt eco-friendly lifestyle choices", ["Because individuals have no impact alone", "Because the Earth will fix itself without human action", "Because children are the only ones affected"])
        ]
    }

    # Generate Chapters 11, 12, 13
    for ch_num, cases_dict in [(11, ch11_cases), (12, ch12_cases), (13, ch13_cases)]:
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
