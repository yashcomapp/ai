# -*- coding: utf-8 -*-
"""
Generate 82 Canonical Questions for MH-9-SCIT-18-18.4
Topic: Space Telescopes (Hubble, Chandra) & ISRO Space Technology
40 Exam + 30 Practice + 12 Mock/Foundation with Dark-Themed Vector SVGs
"""

import json
import os

TOPIC_CODE = "MH-9-SCIT-18-18.4"

def make_q(qcode, topic, text, options, answer_letter, qtype, difficulty, vault, category, explanation):
    return {
        "questionCode": qcode,
        "topicCode": topic,
        "text": text,
        "options": options,
        "correctAnswer": answer_letter,
        "type": qtype,
        "difficulty": difficulty,
        "vault": vault,
        "examCategory": category,
        "explanation": explanation
    }

# 40 EXAM QUESTIONS (1-40)
exam_data = [
    # 1
    ("Why must astronomical observatories for X-rays and gamma rays be placed above Earth's atmosphere?",
     ["Earth's atmosphere completely absorbs high-energy X-rays and gamma rays, preventing them from reaching ground-based detectors",
      "Because cosmic rays are scared of clouds",
      "Because Earth's gravity destroys X-ray photons",
      "Because ground telescopes are too heavy to point upward"],
     "A", "OSC", "easy",
     "The ozone layer, nitrogen, and oxygen in Earth's atmosphere act as a dense shield that absorbs incoming high-energy radiation such as X-rays and gamma rays, making direct ground detection impossible."),

    # 2
    ("Which key atmospheric effect causes stars to 'twinkle' and degrades the sharpness of ground-based optical telescopes?",
     ["Turbulent air currents with varying temperatures and densities that constantly refract starlight along fluctuating paths",
      "Solar wind physically pushing the stars back and forth",
      "The moon's magnetic field vibrating light waves",
      "Dust grains blocking light in fixed rhythms"],
     "A", "OSC", "easy",
     "Atmospheric seeing is caused by continuous temperature and density gradients in Earth's air layers. These turbulent pockets bend starlight rapidly in random directions, blurring pinpoint stellar images into smeared disks."),

    # 3
    ("In which year was the historic Hubble Space Telescope (HST) launched into low Earth orbit?",
     ["1990", "1969", "2005", "1980"],
     "A", "OSC", "easy",
     "The Hubble Space Telescope was carried into space on 24 April 1990 by Space Shuttle Discovery (mission STS-31) and deployed into low Earth orbit at an altitude of approximately 540–570 km."),

    # 4
    ("What is the diameter of the primary mirror of the Hubble Space Telescope?",
     ["2.4 meters (94 inches)", "10 meters", "0.5 meters", "25 meters"],
     "A", "OSC", "easy",
     "Hubble's primary collecting optic is a concave hyperbolic mirror with a diameter of exactly 2.4 meters, polished to extraordinary smoothness with surface deviations smaller than a fraction of the wavelength of light."),

    # 5
    ("What optical telescope design is employed by the Hubble Space Telescope?",
     ["Ritchey-Chretien Cassegrain reflector with hyperbolic primary and secondary mirrors",
      "Newtonian reflector with a flat diagonal mirror",
      "Simple Galilean refractor with convex objective and concave eyepiece",
      "Herschelian off-axis reflector"],
     "A", "OSC", "medium",
     "Hubble utilizes a specialized Cassegrain configuration called the Ritchey-Chretien design. By using two hyperbolic mirrors, it eliminates both spherical aberration and off-axis coma, providing an exceptionally wide and sharp field of view."),

    # 6
    ("What primary electromagnetic wavebands does the Hubble Space Telescope observe?",
     ["Visible light, near-ultraviolet, and near-infrared",
      "Gamma rays and hard X-rays only",
      "Long-wavelength AM radio waves only",
      "Microwaves and low-frequency radio waves only"],
     "A", "OSC", "easy",
     "Hubble is designed as an optical-ultraviolet-infrared observatory, covering wavelengths from roughly 115 nm (far-ultraviolet) through the visible spectrum to 2500 nm (near-infrared)."),

    # 7
    ("The Chandra X-ray Observatory launched by NASA in 1999 was named in honor of which Nobel Prize-winning Indian-American astrophysicist?",
     ["Subrahmanyan Chandrasekhar", "Sir C. V. Raman", "Homi J. Bhabha", "Jagadish Chandra Bose"],
     "A", "OSC", "easy",
     "Chandra was named in honor of Subrahmanyan Chandrasekhar, who won the 1983 Nobel Prize in Physics for his mathematical theories on the structure and evolution of stars, including the famous Chandrasekhar mass limit."),

    # 8
    ("What is the numerical value of the Chandrasekhar limit in astrophysics?",
     ["Approximately 1.44 solar masses (1.44 M_sun)",
      "Exactly 5.0 solar masses",
      "0.5 solar masses",
      "100 solar masses"],
     "A", "OSC", "easy",
     "The Chandrasekhar limit (~1.44 solar masses) is the maximum mass that electron degeneracy pressure can support in a stable white dwarf star. Beyond this mass, the white dwarf collapses into a neutron star or black hole."),

    # 9
    ("Why cannot ordinary glass or metal mirrors be used at normal perpendicular incidence to reflect cosmic X-rays in Chandra?",
     ["High-energy X-ray photons possess extremely short wavelengths that penetrate into mirror surfaces and are absorbed rather than reflected",
      "X-rays are magnetically repelled by glass",
      "X-rays only reflect off liquid water",
      "Glass mirrors heat up and instantly vaporize when struck by faint starlight"],
     "A", "OSC", "medium",
     "Because X-rays have wavelengths comparable to atomic spacing, they pass straight into matter when striking at steep angles. They can only be reflected when striking mirror surfaces at shallow, grazing angles like skipping stones across water."),

    # 10
    ("What mirror geometry does the Chandra X-ray Observatory employ to focus high-energy X-rays?",
     ["Nested cylindrical Wolter-I mirrors where X-rays ricochet at shallow grazing angles off parabolic and hyperbolic surfaces",
      "A single flat silver-coated plane mirror",
      "A huge double-convex acrylic lens",
      "A spherical plastic prism"],
     "A", "OSC", "medium",
     "Chandra utilizes four nested pairs of cylindrical mirrors (Wolter Type I optics). Incoming X-rays strike the interior surfaces at grazing angles of less than 1 degree, gently skipping onto hyperbolic mirrors that focus the rays onto CCD detectors."),

    # 11
    ("What metal coating covers the ultra-smooth reflecting surfaces of Chandra's nested mirrors to maximize X-ray reflectivity?",
     ["Iridium", "Aluminium foil", "Copper paint", "Lead powder"],
     "A", "OSC", "medium",
     "Chandra's optical barrels are coated with a 30-nanometer layer of iridium (over a chrome binding layer), because high-atomic-number dense metals like iridium provide superior X-ray reflectivity at shallow grazing angles."),

    # 12
    ("What was India's first dedicated multi-wavelength space astronomy observatory launched by ISRO in 2015?",
     ["Astrosat", "Aryabhata", "Chandrayaan-1", "Mangalyaan"],
     "A", "OSC", "easy",
     "Launched on 28 September 2015 aboard PSLV-C30 into a 650 km equatorial orbit, Astrosat is India's first dedicated multi-wavelength space observatory capable of observing optical, UV, and X-ray bands simultaneously."),

    # 13
    ("Which five specialized scientific payloads operate onboard India's Astrosat satellite?",
     ["UVIT, SXT, LAXPC, CZTI, and SSM",
      "Galileo lens, spectroscope, radio antenna, solar sail, and thermometer",
      "Seismograph, barometer, anemometer, rain gauge, and hygrometer",
      "Radar, sonar, lidar, GPS, and compass"],
     "A", "OSC", "medium",
     "Astrosat hosts the Ultraviolet Imaging Telescope (UVIT), Soft X-ray Telescope (SXT), Large Area X-ray Proportional Counter (LAXPC), Cadmium Zinc Telluride Imager (CZTI), and Scanning Sky Monitor (SSM)."),

    # 14
    ("What unique scientific advantage does Astrosat offer by observing celestial targets simultaneously across UV, soft X-ray, and hard X-ray bands?",
     ["It provides continuous correlated multi-wavelength coverage of transient events like black hole accretions and neutron star mergers without inter-instrument delay",
      "It allows astronauts to make live telephone calls to Mars",
      "It replaces all weather forecast satellites",
      "It changes the orbital path of distant comets"],
     "A", "OSC", "medium",
     "Astrosat's concurrent multi-band capability allows astronomers to study high-energy mechanisms (e.g., accretion disks radiating in UV and corona radiating in hard X-rays) in real time without the timing mismatches common to coordinating separate space missions."),

    # 15
    ("In which year was the Indian Space Research Organisation (ISRO) officially founded?",
     ["1969", "1947", "1984", "2000"],
     "A", "OSC", "easy",
     "ISRO was founded on 15 August 1969, superseding the Indian National Committee for Space Research (INCOSPAR) which had been established in 1962 under the Department of Atomic Energy."),

    # 16
    ("Who is revered as the visionary Founding Father of the Indian Space Programme?",
     ["Dr. Vikram Sarabhai", "Dr. Homi Bhabha", "Sir C. V. Raman", "Dr. A. P. J. Abdul Kalam"],
     "A", "OSC", "easy",
     "Dr. Vikram Sarabhai recognized the immense value of space technology for developing nations like India, envisioning satellites for mass education, weather forecasting, telecommunications, and natural resource management."),

    # 17
    ("Where is the primary satellite launching spaceport of ISRO located in India?",
     ["Satish Dhawan Space Centre (SDSC) SHAR at Sriharikota, Andhra Pradesh",
      "Gateway of India, Mumbai",
      "Thumba Equatorial Rocket Launching Station, Kerala",
      "Mount Abu, Rajasthan"],
     "A", "OSC", "easy",
     "Satish Dhawan Space Centre (SDSC) SHAR is located on Sriharikota Island off the coast of Andhra Pradesh; its location near the equator and eastward launch corridor over the Bay of Bengal provides optimal orbital insertion dynamics and safety."),

    # 18
    ("What was the name of India's very first artificial satellite, launched into space on 19 April 1975?",
     ["Aryabhata", "Rohini", "Bhaskara-I", "INSAT-1A"],
     "A", "OSC", "easy",
     "Aryabhata, named after the classical 5th-century Indian astronomer and mathematician, was India's first satellite. It was fabricated by ISRO and launched into space by a Soviet Kosmos-3M launch vehicle from Kapustin Yar."),

    # 19
    ("Which historic satellite in 1980 marked the first time India placed a payload into orbit using an indigenous Indian launch vehicle (SLV-3)?",
     ["Rohini (RS-1)", "Aryabhata", "Apple", "EDUSAT"],
     "A", "OSC", "easy",
     "On 18 July 1980, Satellite Launch Vehicle-3 (SLV-3), under the project leadership of Dr. A. P. J. Abdul Kalam, successfully injected the Rohini RS-1 satellite into Earth orbit, making India the sixth spacefaring nation with independent launch capability."),

    # 20
    ("What primary national service is delivered by ISRO's INSAT (Indian National Satellite System) and GSAT series of geostationary satellites?",
     ["Telecommunications, television broadcasting, meteorological monitoring, and search-and-rescue operations",
      "Mining gold on asteroids",
      "Providing fuel to deep space probes",
      "Drilling oil beneath the ocean floor"],
     "A", "OSC", "easy",
     "The INSAT and GSAT series operate in geostationary orbit (~36,000 km altitude), carrying transponders that provide nation-wide telephone networks, DTH television, cyclone early warnings, and emergency disaster communications."),

    # 21
    ("What is the primary operational mission of the IRS (Indian Remote Sensing) satellite series?",
     ["Earth observation for agriculture, water resources, forestry mapping, mineral prospecting, and coastal oceanography",
      "Searching for alien radio signals in distant galaxies",
      "Broadcasting high-volume FM radio music",
      "Supplying oxygen to commercial aeroplanes"],
     "A", "OSC", "easy",
     "IRS satellites operate in polar Sun-synchronous orbits, imaging India's landmass and oceans in multiple spectral bands to monitor crop health, ground water reserves, urban growth, drought severity, and disaster impacts."),

    # 22
    ("What world-first educational milestone was achieved by ISRO with the launch of EDUSAT (GSAT-3) in September 2004?",
     ["It was the world's first satellite built exclusively to deliver interactive satellite-based distance education to schools and universities",
      "It was the first satellite to carry school students into orbit",
      "It was the first satellite to print physical school textbooks in space",
      "It conducted school exams using laser beams"],
     "A", "OSC", "easy",
     "EDUSAT was specifically dedicated to the education sector, connecting remote classrooms, rural colleges, and teacher training institutes across India via two-way interactive audiovisual satellite terminals."),

    # 23
    ("What monumental scientific discovery was made on the Moon by India's maiden lunar probe, Chandrayaan-1, in 2008?",
     ["Direct proof of water molecules (H2O and OH hydroxyl groups) trapped in lunar soil and polar craters",
      "Rivers of liquid water flowing freely on the lunar equator",
      "Massive forests of green plants",
      "Fossilized dinosaur bones in lunar dust"],
     "A", "OSC", "easy",
     "Chandrayaan-1's Moon Mineralogy Mapper (M3), an imaging spectrometer developed in collaboration with NASA, detected the unequivocal diagnostic spectral absorption signature of water molecules and hydroxyl ions bound to lunar regolith."),

    # 24
    ("What historic global achievement was logged by ISRO's Mars Orbiter Mission (Mangalyaan) in September 2014?",
     ["India became the first nation in the world to successfully place a spacecraft into Martian orbit on its maiden attempt, and at record low cost",
      "Mangalyaan landed human astronauts on Mars",
      "Mangalyaan brought Martian soil rocks back to Earth",
      "Mangalyaan built a permanent research colony on Mars"],
     "A", "OSC", "easy",
     "Mangalyaan reached Mars on 24 September 2014 on its very first try—a feat neither the USA, Russia, nor Europe achieved on their maiden missions—at a frugal cost of ~₹450 crore ($74 million), less than the budget of many Hollywood space movies."),

    # 25
    ("On which historic date did ISRO's Chandrayaan-3 land its Vikram lander near the Moon's South Pole, leading India to declare 'National Space Day'?",
     ["23 August 2023", "15 August 2020", "26 January 2022", "14 July 2023"],
     "A", "OSC", "easy",
     "On 23 August 2023, Chandrayaan-3's Vikram lander achieved a flawless soft landing at 69.37° S latitude near the lunar south pole, making India the first country to land in the south polar region and the fourth to soft-land on the Moon."),

    # 26
    ("What are the names of the lander and rover components of the Chandrayaan-3 mission?",
     ["Lander: Vikram; Rover: Pragyan",
      "Lander: Aryabhata; Rover: Bhaskara",
      "Lander: Rohini; Rover: Sarabhai",
      "Lander: Aditya; Rover: Kalam"],
     "A", "OSC", "easy",
     "The lander was named Vikram (meaning 'valour', after Dr. Vikram Sarabhai) and the 6-wheeled robotic rover was named Pragyan (Sanskrit for 'wisdom')."),

    # 27
    ("What is the primary scientific mission of ISRO's Aditya-L1 solar observatory launched in September 2023?",
     ["Studying the Sun's dynamic outer atmosphere (chromosphere and corona), coronal mass ejections (CMEs), and space weather",
      "Landing a rover on the Sun's solid surface",
      "Extinguishing solar flares using water tanks",
      "Collecting samples of hot lava from the Sun"],
     "A", "OSC", "easy",
     "Aditya-L1 was inserted into a halo orbit around the Sun-Earth Lagrangian Point 1 (L1), 1.5 million km from Earth, to continuously observe the solar corona, solar wind acceleration, and magnetic storms without any eclipse interruptions."),

    # 28
    ("Why is Lagrangian Point 1 (L1) chosen for solar observatories like Aditya-L1?",
     ["Gravitational forces of the Sun and Earth balance the orbital motion of the spacecraft, providing an unobstructed, continuous view of the Sun without occultation",
      "L1 is located inside Earth's magnetic core",
      "L1 is completely shielded from solar heat",
      "L1 is close enough to touch the Moon's surface"],
     "A", "OSC", "medium",
     "At Lagrange Point 1, the gravitational pulls of the Sun and Earth provide precisely the centripetal force required for a satellite to orbit in sync with Earth, ensuring the Sun is never blocked by Earth or the Moon."),

    # 29
    ("What is the primary objective of ISRO's flagship human spaceflight programme named 'Gaganyaan'?",
     ["To demonstrate indigenous human spaceflight capability by launching a crew of astronauts to low Earth orbit (400 km) and safely returning them to Earth",
      "To send tourists to the rings of Saturn",
      "To build a high-speed bullet train between Earth and the Moon",
      "To relocate all humans to Mars by 2030"],
     "A", "OSC", "easy",
     "Gaganyaan is designed to demonstrate human spaceflight capability by launching a 3-member crew into a 400 km circular orbit for a 3-day mission, followed by a safe splashdown in Indian territorial waters."),

    # 30
    ("What orbital altitude range does the Hubble Space Telescope occupy above Earth?",
     ["Approximately 540 to 570 kilometers (Low Earth Orbit)",
      "36,000 kilometers (Geostationary Orbit)",
      "384,400 kilometers (Lunar Orbit)",
      "1,500,000 kilometers (Lagrange Point 2)"],
     "A", "OSC", "easy",
     "Hubble orbits Earth in Low Earth Orbit (LEO) at an altitude of ~540 km with an orbital period of approximately 95 minutes, completing roughly 15 orbits around Earth each day."),

    # 31
    ("Why did the Hubble Space Telescope produce slightly blurry images immediately after its deployment in 1990?",
     ["Its primary mirror suffered from spherical aberration due to an edge ground too flat by just 2.2 micrometers (about 1/50th of a human hair)",
      "The mirror was completely broken into shards during launch",
      "Space dust covered the lens within five minutes of launch",
      "The telescope pointed backwards toward Earth instead of space"],
     "A", "OSC", "medium",
     "A flawed optical testing tool (null corrector) caused Perkin-Elmer to grind Hubble's primary mirror perimeter 2 microns too flat; this spherical aberration was brilliantly corrected in 1993 during the STS-61 servicing mission using COSTAR corrective optics."),

    # 32
    ("How does the angular resolution of a space telescope compare to an identical ground-based telescope without adaptive optics?",
     ["The space telescope achieves diffraction-limited angular resolution unhampered by atmospheric blur, resolving far finer cosmic details",
      "The space telescope is ten times blurrier because space is dark",
      "There is no difference in resolution between ground and space",
      "The ground telescope is always sharper because it is closer to astronomers"],
     "A", "OSC", "easy",
     "Free from atmospheric turbulence (which limits ground telescopes to a seeing resolution of ~0.5–1.0 arcseconds), Hubble achieves its theoretical optical diffraction limit of roughly 0.05 arcseconds—a tenfold improvement in sharpness."),

    # 33
    ("Which space observatory launched in 2021 as the scientific successor to Hubble operates primarily in the infrared spectrum at Lagrange Point 2 (L2)?",
     ["James Webb Space Telescope (JWST)", "Spitzer Space Telescope", "Kepler Space Telescope", "Fermi Gamma-ray Telescope"],
     "A", "OSC", "easy",
     "The James Webb Space Telescope (JWST), featuring a 6.5-meter gold-coated beryllium segmented primary mirror, was launched in December 2021 to observe high-redshift early galaxies and exoplanet atmospheres in infrared from Sun-Earth L2."),

    # 34
    ("What launch vehicle is known as the reliable 'Workhorse of ISRO', having launched Chandrayaan-1, Mangalyaan, and Astrosat?",
     ["PSLV (Polar Satellite Launch Vehicle)", "SLV-3", "ASLV", "Sounding Rocket Rohini-75"],
     "A", "OSC", "easy",
     "The Polar Satellite Launch Vehicle (PSLV), with its versatile 4-stage solid/liquid propulsion configuration and strap-on boosters, has maintained an extraordinary success record of over 95%, launching dozens of Indian and international spacecraft."),

    # 35
    ("What is the primary role of India's heavy-lift rocket, the LVM3 (Launch Vehicle Mark-3, formerly GSLV Mk III)?",
     ["Injecting heavy 4-tonne communication satellites into GTO and launching interplanetary payloads like Chandrayaan-2 and Chandrayaan-3",
      "Launching toy gliders into neighborhood parks",
      "Delivering commercial mail across Indian cities",
      "Propelling submarines beneath polar ice caps"],
     "A", "OSC", "easy",
     "LVM3 is India's most powerful three-stage rocket, featuring twin massive S200 solid strap-on boosters, an L110 core liquid stage, and the indigenous CE-20 cryogenic upper stage capable of lifting 4 tonnes to GTO and 8 tonnes to LEO."),

    # 36
    ("What is the orbital period of a geostationary satellite such as those in the INSAT and GSAT constellations?",
     ["23 hours, 56 minutes, 4 seconds (1 sidereal day)",
      "90 minutes",
      "12 hours",
      "30 days"],
     "A", "OSC", "easy",
     "A geostationary satellite circles Earth in the equatorial plane at the exact same angular velocity as Earth's rotation (one sidereal day), so it appears stationary from any spot on Earth, allowing fixed ground dish antennas."),

    # 37
    ("What major atmospheric advantage allows space telescopes to observe continuously without daytime interruptions?",
     ["In the vacuum of orbit, there is no atmospheric Rayleigh scattering of sunlight to turn the daytime sky bright blue",
      "Because the Sun stops shining whenever a satellite is in orbit",
      "Because space telescopes wear dark sunglasses",
      "Because space has no photons"],
     "A", "OSC", "medium",
     "On Earth, sunlight scattered by air molecules illuminates the sky during daytime; in the vacuum of space, the sky remains jet-black at all times, allowing space telescopes pointing away from the Sun to record faint cosmic targets continuously."),

    # 38
    ("Which celestial objects emit intense high-energy X-rays studied by space observatories like Chandra and Astrosat?",
     ["Accretion disks around black holes, neutron stars, supernova remnants, and hot gas in galaxy clusters",
      "Ordinary cold rocks lying on Mars",
      "Deep ocean trenches on Earth",
      "Ice crystals inside Saturn's rings"],
     "A", "OSC", "easy",
     "Thermal X-rays are produced by matter heated to millions of degrees, such as plasma swirling violently into black hole accretion disks, supernova shock fronts, and diffuse intergalactic gas trapped in giant galaxy clusters."),

    # 39
    ("What was the significance of the payload instrument named 'LIBS' (Laser-Induced Breakdown Spectroscopy) onboard the Pragyan rover during Chandrayaan-3?",
     ["It confirmed the presence of Sulfur (S) and other chemical elements on the lunar surface near the South Pole using laser plasma emission",
      "It drilled a 10-kilometer hole into the Moon's center",
      "It painted the Indian flag onto lunar rocks",
      "It played national anthems on the Moon"],
     "A", "OSC", "medium",
     "Pragyan's LIBS fired intense laser pulses onto lunar rocks to generate high-temperature plasma; analyzing the emitted spectral lines confirmed the unambiguous presence of Sulfur, Aluminium, Calcium, Iron, and Titanium in the polar regolith."),

    # 40
    ("Which Indian satellite navigation constellation, developed indigenously by ISRO, provides independent satellite positioning across India and up to 1,500 km beyond its borders?",
     ["NavIC (Navigation with Indian Constellation / IRNSS)",
      "GPS", "GLONASS", "Galileo"],
     "A", "OSC", "easy",
     "NavIC (Navigation with Indian Constellation) consists of an independent regional constellation of 7 geostationary and geosynchronous satellites that delivers high-accuracy positioning services for civil aviation, maritime navigation, and defense.")
]

# 30 PRACTICE QUESTIONS (41-70)
practice_data = [
    # 41
    ("Why is infrared astronomy particularly hindered by Earth's atmosphere?",
     ["Atmospheric water vapor and carbon dioxide strongly absorb infrared wavelengths, and the warm atmosphere itself glows with thermal infrared background noise",
      "Infrared photons are too heavy to fall through air",
      "Air turns infrared photons into sound waves",
      "Infrared light is destroyed by atmospheric nitrogen"],
     "A", "OSC", "medium",
     "Earth's atmosphere absorbs most infrared bands due to H2O and CO2 molecules. Furthermore, ambient air at ~300 K radiates thermal infrared glow, drowning out faint deep-space infrared sources like a bright lamp in fog."),

    # 42
    ("How does the primary mirror of the Hubble Space Telescope achieve high reflectivity across ultraviolet and visible light?",
     ["It is coated with an ultra-thin layer of pure aluminium (approx 65 nm) sealed under a protective magnesium fluoride (MgF2) layer to prevent oxidation",
      "It is painted with ordinary silver household paint",
      "It is made of pure clear diamond",
      "It is polished with liquid mercury"],
     "A", "OSC", "medium",
     "Aluminium provides high reflectivity from far-UV to near-IR; because aluminium oxidizes instantly in air, a protective 25 nm layer of magnesium fluoride (MgF2) is deposited over it to prevent oxidation and maintain UV transmittance."),

    # 43
    ("What is the primary scientific reason why Chandra X-ray Observatory's orbit is highly elliptical (apogee ~140,000 km)?",
     ["To keep the satellite outside Earth's Van Allen radiation belts for over 75% of its 64-hour orbit, enabling uninterrupted low-background X-ray observations",
      "To allow the spacecraft to swing around Mars for fun",
      "To save fuel by letting the Moon pull it sideways",
      "Because circular orbits are illegal for X-ray satellites"],
     "A", "OSC", "hard",
     "Earth's Van Allen belts contain dense trapped protons and electrons that overwhelm sensitive X-ray detectors with particle background noise; Chandra's high apogee (~1/3 the distance to the Moon) keeps it far above the belts for most of each orbit."),

    # 44
    ("What critical role does the Ultra-Violet Imaging Telescope (UVIT) play onboard India's Astrosat?",
     ["It captures high-resolution images in the far-ultraviolet (FUV) and near-ultraviolet (NUV) bands, resolving star-forming regions in distant galaxies",
      "It takes colour photos of Indian cities for tourist brochures",
      "It measures the temperature of seawater in the Bay of Bengal",
      "It beams television signals to remote villages"],
     "A", "OSC", "medium",
     "Astrosat's UVIT consists of twin 37 cm aperture telescopes observing from 130 nm to 300 nm, providing sub-1.5-arcsecond angular resolution to map young, hot, massive stars and active galactic nuclei."),

    # 45
    ("Which law of planetary motion formulated by Johannes Kepler governs the elliptical transfer orbit used by Mangalyaan to travel from Earth to Mars?",
     ["Kepler's First Law (elliptical orbit with the Sun at one focus) and Third Law (orbital period relation)",
      "Newton's Law of Universal Gravitation only",
      "Hooke's Law of Elasticity",
      "Boyle's Gas Law"],
     "A", "OSC", "medium",
     "Mangalyaan used a Hohmann transfer ellipse: an elliptical trajectory whose perihelion is at Earth's orbit and aphelion is at Mars' orbit, governed precisely by Kepler's laws of planetary motion with the Sun at one focus."),

    # 46
    ("What was the primary function of the Moon Impact Probe (MIP) released by Chandrayaan-1 on 14 November 2008?",
     ["It descended through the lunar exosphere and impacted near Shackleton Crater at the South Pole, directly sniffing water vapor in the lunar thin atmosphere",
      "It planted an explosive charge to break the Moon apart",
      "It bounced off the Moon and flew toward Jupiter",
      "It beamed FM radio music to Earth"],
     "A", "OSC", "medium",
     "The Moon Impact Probe carried a quadrupole mass spectrometer (CHACE) that recorded the altitude profile of lunar gas species during its 25-minute descent, detecting direct mass-spectrometric evidence of water vapor before impacting near the South Pole."),

    # 47
    ("Why did ISRO use the clever 'gravity-assist' slingshot and orbital raising manoeuvres for Mangalyaan rather than a direct injection to Mars?",
     ["To compensate for the lower lift capacity of the PSLV rocket by using Earth's gravitational pull and multiple perigee burns to build escape velocity fuel-efficiently",
      "Because the rocket was launched backwards",
      "Because Mars was moving away from the Sun",
      "Because ISRO ran out of rocket fuel on launch day"],
     "A", "OSC", "medium",
     "PSLV could not launch Mangalyaan directly onto a trans-Mars injection trajectory in a single burn; ISRO engineers brilliantly used 6 successive perigee rocket firings to expand its elliptical Earth orbit, gradually building velocity using minimal fuel."),

    # 48
    ("What temperature range must cryogenic rocket engines utilize for their liquid fuel and oxidizer components?",
     ["Liquid Hydrogen at -253 deg C and Liquid Oxygen at -183 deg C",
      "Boiling water at +100 deg C and diesel at +20 deg C",
      "Liquid helium at room temperature +25 deg C",
      "Molten iron at +1500 deg C"],
     "A", "OSC", "medium",
     "Cryogenic rocketry uses liquefied gases at extreme sub-zero temperatures: liquid hydrogen (fuel) boils at -253 °C (20 K) and liquid oxygen (oxidizer) boils at -183 °C (90 K), delivering exceptionally high specific impulse."),

    # 49
    ("What is the primary role of the Indian Deep Space Network (IDSN) station established at Byalalu near Bengaluru?",
     ["Tracking, commanding, and receiving high-frequency telemetry and scientific data from deep space missions like Chandrayaan and Mangalyaan",
      "Broadcasting high-definition television sports channels",
      "Controlling streetlights in Bengaluru city",
      "Monitoring internet cables across the Indian Ocean"],
     "A", "OSC", "easy",
     "IDSN at Byalalu hosts giant 18-meter and 32-meter parabolic dish antennas equipped with cryogenic low-noise receivers to track and command spacecraft millions of kilometers away across interplanetary space."),

    # 50
    ("What is the primary payload of the Astrosat Large Area X-ray Proportional Counter (LAXPC)?",
     ["High-temporal-resolution timing studies of rapid fluctuations and pulsations in cosmic X-ray binary systems (3 to 80 keV)",
      "Measuring rainfall over the Himalayan mountain range",
      "Recording ambient starlight colors for art painting",
      "Mapping the magnetic polarity of Earth's north pole"],
     "A", "OSC", "hard",
     "LAXPC has an exceptionally large collecting area of ~6000 cm^2 and sub-millisecond time resolution, making it one of the world's most sensitive instruments for detecting millisecond quasi-periodic oscillations (QPOs) in black hole and neutron star binaries."),

    # 51
    ("Which physical principle explains why space telescopes in vacuum do not experience mechanical vibrations from aerodynamic wind?",
     ["Vacuum contains no fluid medium (air molecules) to transfer aerodynamic drag or turbulent pressure fluctuations",
      "Telescope mirrors are made of magic metals that repel air",
      "Gravity ceases to exist in outer space",
      "Wind only blows downward toward the ground"],
     "A", "OSC", "easy",
     "In the high vacuum of orbital space (~10^-7 Pa), aerodynamic drag is negligible and there are no atmospheric gusts, eliminating the wind-induced buffeting and structural jitter that plague ground-based telescopes."),

    # 52
    ("Why must space telescopes like Chandra and Hubble use reaction wheels and gyroscopes rather than rudder fins to turn and aim at targets?",
     ["In the vacuum of space, aerodynamic fins have no air to push against; conservation of angular momentum allows internal spinning reaction wheels to torque the spacecraft",
      "Because fins would fall off under extreme space cold",
      "Because rocket propellers are forbidden in orbit",
      "Because reaction wheels generate electricity from starlight"],
     "A", "OSC", "medium",
     "Without an atmosphere, aerodynamic control surfaces are completely useless. By accelerating or decelerating heavy, spinning internal flywheels (reaction wheels), the spacecraft exerts an equal and opposite torque on itself via conservation of angular momentum."),

    # 53
    ("What is the primary objective of the XPoSat (X-ray Polarimeter Satellite) launched by ISRO in January 2024?",
     ["Measuring the polarization of cosmic X-rays from black holes, neutron stars, and supernova remnants to understand their magnetic geometry",
      "Searching for underground water springs on Earth",
      "Testing solar panels for future electric cars",
      "Measuring the temperature of the upper atmosphere"],
     "A", "OSC", "medium",
     "XPoSat is India's first dedicated polarimetry space mission (and only the world's second after NASA's IXPE), measuring the degree and angle of polarization of X-rays (8-30 keV) to map extreme magnetic fields around pulsars and black holes."),

    # 54
    ("What distinguishes a geostationary orbit (GEO) from a polar Sun-synchronous orbit (SSO)?",
     ["GEO is equatorial at 36,000 km altitude with a 24-hour period; SSO is a near-polar orbit at 600-800 km altitude crossing the equator at the same local solar time daily",
      "GEO is on the Moon's surface; SSO is on the Sun's surface",
      "GEO orbits every 90 minutes; SSO orbits once per year",
      "GEO is only used for submarines; SSO is used for aeroplanes"],
     "A", "OSC", "medium",
     "GEO matches Earth's rotation to stay fixed above one spot on the equator, ideal for communications; SSO orbits over the poles at low altitude, passing over each latitude at identical illumination conditions, ideal for remote sensing."),

    # 55
    ("What protective mechanism protects space telescopes from the extreme temperature swings (+120 deg C in sunlight to -150 deg C in Earth shadow)?",
     ["Multi-layer insulation (MLI) reflective thermal blankets and active electric heaters with thermostatic controls",
      "Air conditioning units running on liquid gasoline",
      "Thick layers of ordinary building brick insulation",
      "Coating the telescope in running tap water"],
     "A", "OSC", "medium",
     "Spacecraft use Multi-Layer Insulation (MLI)—stacks of aluminized Mylar or Kapton separated by scrim netting—to reflect solar radiation and prevent thermal radiative loss into deep space, paired with precision heaters to keep optics dimensionally stable."),

    # 56
    ("What is the function of the solar panels onboard space observatories like Hubble, Astrosat, and Chandra?",
     ["Converting solar radiant energy into electrical energy to power on-board computers, sensors, scientific instruments, and recharge batteries",
      "Reflecting starlight toward Earth for evening illumination",
      "Acting as giant sails to blow the spacecraft to Mars",
      "Cooling the satellite by shading it from the Sun"],
     "A", "OSC", "easy",
     "Photovoltaic solar arrays convert incident sunlight into electrical power (Hubble produces ~2800 W), powering telemetry, attitude control systems, and scientific detectors while recharging nickel-hydrogen batteries for operation in Earth's shadow."),

    # 57
    ("Why do space telescopes require ultra-high pointing stability (e.g. Hubble stabilizes to within 0.007 arcseconds)?",
     ["Long exposure times needed to capture photons from ultra-faint distant galaxies would become hopelessly blurred if the telescope drifted even slightly",
      "To prevent the satellite from falling out of orbit",
      "Because starlight moves sideways at high speeds",
      "To keep the telescope pointed away from the Moon"],
     "A", "OSC", "medium",
     "Deep-field exposures require staring at a tiny patch of sky for hours or days; any tracking jitter greater than a few milli-arcseconds would smear the photons across multiple detector pixels, destroying the razor-sharp diffraction-limited resolution."),

    # 58
    ("What chemical propellant combination is used in the liquid second stage (Vikas engine) of ISRO's PSLV rocket?",
     ["Unsymmetrical Dimethylhydrazine (UDMH) as fuel and Dinitrogen Tetroxide (N2O4) as oxidizer",
      "Petrol and liquid air",
      "Kerosene and ordinary room air",
      "Liquid hydrogen and charcoal powder"],
     "A", "OSC", "hard",
     "The Vikas engine (PS2 stage) burns hypergolic storable liquid propellants: UDMH with 25% Hydrazine hydrate (UH25) and N2O4, which ignite spontaneously on contact without requiring an external igniter."),

    # 59
    ("What major milestone did ISRO achieve on 15 February 2017 aboard flight PSLV-C37?",
     ["Successfully deployed a world-record 104 satellites into orbit in a single mission",
      "Launched the first manned rocket to the Moon",
      "Landed a spacecraft on Venus",
      "Retrieved an old satellite from deep space back to Earth"],
     "A", "OSC", "easy",
     "PSLV-C37 created a historic world record by precisely launching 104 satellites (including Cartosat-2D and 103 co-passenger nanosatellites from 6 nations) into polar Sun-synchronous orbit from Sriharikota."),

    # 60
    ("What is the function of the Star Trackers mounted on space telescopes and ISRO satellites?",
     ["Optical cameras that match observed star constellations with onboard celestial catalogs to determine the satellite's exact 3-axis orientation in space",
      "Telescopes used by astronomers to find newly born stars",
      "Lasers used to shoot down space debris",
      "Sensors that detect alien spaceships"],
     "A", "OSC", "medium",
     "Star trackers image background star fields and compare angular separations against an internal database of tens of thousands of stars, computing the satellite's orientation (attitude) with arcsecond accuracy in real time."),

    # 61
    ("Why do X-ray telescopes like Chandra and Astrosat use grazing angles typically less than 1 to 2 degrees?",
     ["At larger angles, X-ray photon energies exceed the critical angle for total external reflection and penetrate into the mirror bulk rather than bouncing off",
      "Because larger angles make the mirrors too heavy",
      "Because X-rays turn into visible light at 5 degrees",
      "Because mirrors melt when struck by starlight at 45 degrees"],
     "A", "OSC", "hard",
     r"The refractive index of matter for X-rays is slightly less than unity ($n = 1 - \delta$, where $\delta \approx 10^{-5}$); total external reflection can only occur when the grazing angle $\theta < \sqrt{2\delta}$, which is typically less than 1 degree."),

    # 62
    ("What was the unique accomplishment of the payload 'ChaSTE' (Chandra's Surface Thermophysical Experiment) on Chandrayaan-3's Vikram lander?",
     ["It inserted a thermal probe 10 cm into lunar polar soil, measuring the first-ever vertical temperature gradient from +50 deg C on the surface to -10 deg C just below",
      "It heated the lunar surface to boil water for tea",
      "It measured the core temperature of the Moon's center",
      "It discovered burning volcanic lava under the south pole"],
     "A", "OSC", "medium",
     "ChaSTE drove a penetration probe with 10 temperature sensors into lunar regolith, revealing that lunar soil is an extraordinary thermal insulator: surface temperature was ~50 °C, but plummeted to -10 °C just 8 cm below the surface."),

    # 63
    ("Which space observatory discovered that the expansion rate of the universe is actually accelerating, driven by dark energy?",
     ["Hubble Space Telescope (through Type Ia supernovae observations)",
      "Astrosat", "Aryabhata", "EDUSAT"],
     "A", "OSC", "easy",
     "In 1998, observations of distant Type Ia supernovae by teams using Hubble and ground telescopes revealed that cosmic expansion is accelerating, pointing to the existence of dark energy (earning the 2011 Nobel Prize in Physics)."),

    # 64
    ("What makes the CE-20 cryogenic engine developed by ISRO's Liquid Propulsion Systems Centre (LPSC) a technical masterpiece?",
     ["It operates on a gas-generator cycle producing 200 kN of thrust using Liquid Oxygen and Liquid Hydrogen, powering the upper stage of LVM3",
      "It uses compressed air and kerosene to launch kites",
      "It runs on ordinary solar power without any chemical combustion",
      "It uses nuclear fusion to reach Mars in ten minutes"],
     "A", "OSC", "hard",
     "The indigenous CE-20 is one of the world's most powerful gas-generator cycle cryogenic upper-stage engines, burning LH2/LOX to deliver high specific impulse (~443 seconds), vital for heavy-lift missions like Chandrayaan-3 and Gaganyaan."),

    # 65
    ("What is space debris (orbital junk), and why does it pose a serious hazard to space telescopes in low Earth orbit?",
     ["Defunct satellites, rocket stages, and fragments moving at orbital speeds (~7.8 km/s), where even a 1-cm paint fleck carries kinetic energy comparable to a hand grenade",
      "Dust from meteors that dissolves satellite metal",
      "Radio waves floating in space that jam telescope mirrors",
      "Clouds of steam produced by burning rocket engines"],
     "A", "OSC", "easy",
     "In Low Earth Orbit, orbital velocities are around 28,000 km/h (7.8 km/s); at this velocity, collision with even a tiny bolt or metal fragment delivers devastating explosive kinetic energy ($E_k = \frac{1}{2}mv^2$), puncturing solar panels or shattering mirrors."),

    # 66
    ("What payload on Astrosat detected UV photons from a galaxy located 9.3 billion light-years away, called AUDFs01?",
     ["UVIT (Ultra-Violet Imaging Telescope)", "LAXPC", "SSM", "CZTI"],
     "A", "OSC", "medium",
     "In 2020, an international team led by IUCAA Pune used Astrosat's UVIT to discover extreme-ultraviolet light from a galaxy (AUDFs01) 9.3 billion light-years away, an epoch when the universe was in its peak star-formation era."),

    # 67
    ("What is the primary role of the Indian Space Science Data Centre (ISSDC) located at Byalalu, Bengaluru?",
     ["Ingesting, processing, archiving, and disseminating scientific data from India's space science missions (Chandrayaan, Mangalyaan, Astrosat, Aditya-L1) to global researchers",
      "Printing space stamps for the postal department",
      "Selling satellite photographs to social media companies",
      "Manufacturing launch vehicle rocket engines"],
     "A", "OSC", "easy",
     "ISSDC is the centralized data repository for ISRO's space science payloads, processing raw spacecraft telemetry into calibrated datasets and hosting open data archives for the worldwide astronomical research community."),

    # 68
    ("Why are space telescopes insulated against stray light with long baffled sunshades / light shields extending forward of the primary mirror?",
     ["To block off-axis sunlight, moonlight, and Earth-shine from reflecting directly into the telescope tube and overwhelming faint cosmic targets",
      "To prevent birds from nesting inside the telescope",
      "To keep rain from falling onto the glass mirror",
      "To act as a magnifying lens for nearby planets"],
     "A", "OSC", "easy",
     "Even a minuscule fraction of bright sunlight or Earth-shine scattering off mirror edges into the focal plane would wash out astronomical targets that are trillions of times fainter; cylindrical baffles ensure only parallel on-axis cosmic rays enter."),

    # 69
    ("What is meant by the 'Chandrasekhar mass limit' in the life cycle of stars?",
     ["The maximum upper mass limit (~1.44 solar masses) of a non-rotating white dwarf supported by electron degeneracy pressure before collapsing",
      "The minimum mass required for a cloud of gas to form a star",
      "The total mass of the Milky Way galaxy",
      "The mass of Earth's atmosphere"],
     "A", "OSC", "easy",
     "Derived by S. Chandrasekhar in 1930 using special relativity and quantum mechanics, it proves that if a burnt-out stellar core exceeds 1.44 solar masses, electron degeneracy pressure fails and the core collapses into a neutron star or black hole."),

    # 70
    ("What is the primary advantage of placing space telescopes in a halo orbit around Lagrange Point 2 (L2), like JWST?",
     ["Earth, Moon, and Sun stay clustered in the same direction behind the telescope, allowing a single deployable sunshield to permanently block their light and heat",
      "L2 is located inside a heated vacuum chamber in space",
      "Gravity is completely zero at L2 so mirrors don't need frames",
      "Astronauts can easily walk to L2 without spacesuits"],
     "A", "OSC", "medium",
     "At L2 (1.5 million km anti-sunward), the Sun, Earth, and Moon always remain aligned in one direction. A spacecraft can point its heat shield continuously toward them while its optics face the undisturbed, ultra-cold deep sky 24 hours a day.")
]

# 12 MOCK / FOUNDATION QUESTIONS (71-82) WITH DARK-THEMED VECTOR SVGS
mock_data = [
    # 71: Why Space Telescopes? Atmospheric Transmission Windows
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#090d16"/>
  <!-- Space Zone (Top) -->
  <rect x="20" y="20" width="360" height="40" rx="4" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="200" y="45" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">SPACE (Vacuum: 100% All Wavelengths Accessible!)</text>
  <!-- Atmospheric Absorption Layer (Middle) -->
  <rect x="20" y="65" width="360" height="65" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
  <text x="200" y="80" fill="#f87171" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">EARTH ATMOSPHERE (Absorbs Gamma, X-rays, UV & Most IR)</text>
  <!-- Ray Beams: Gamma/X-ray (Blocked) -->
  <line x1="60" y1="25" x2="60" y2="85" stroke="#ef4444" stroke-width="3"/>
  <line x1="53" y1="80" x2="67" y2="90" stroke="#ef4444" stroke-width="2"/>
  <line x1="67" y1="80" x2="53" y2="90" stroke="#ef4444" stroke-width="2"/>
  <text x="60" y="105" fill="#fca5a5" font-size="7" font-family="sans-serif" text-anchor="middle">X-rays Blocked</text>
  <!-- Ray Beams: Optical (Passes Through) -->
  <line x1="160" y1="25" x2="160" y2="155" stroke="#4ade80" stroke-width="3"/>
  <polygon points="160,155 155,145 165,145" fill="#4ade80"/>
  <text x="160" y="105" fill="#86efac" font-size="7" font-family="sans-serif" text-anchor="middle">Visible Light Window</text>
  <!-- Ray Beams: Radio (Passes Through) -->
  <line x1="260" y1="25" x2="260" y2="155" stroke="#facc15" stroke-width="3"/>
  <polygon points="260,155 255,145 265,145" fill="#facc15"/>
  <text x="260" y="105" fill="#fef08a" font-size="7" font-family="sans-serif" text-anchor="middle">Radio Window</text>
  <!-- Ground Level (Bottom) -->
  <rect x="20" y="135" width="360" height="45" rx="4" fill="#14532d" stroke="#4ade80" stroke-width="1.5"/>
  <text x="200" y="165" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">GROUND SURFACE: Only Optical & Radio Windows Reach Detectors</text>
  <!-- Footer Note -->
  <text x="200" y="192" fill="#cbd5e1" font-size="7" font-family="sans-serif" text-anchor="middle">Space telescopes are irreplaceable for X-ray, Gamma, UV, and Far-IR astronomy!</text>
</svg>
</div>
Based on the electromagnetic atmospheric opacity diagram above, why must observatories for X-rays and ultraviolet light be launched into space?""",
     ["Earth's atmosphere completely blocks incoming X-rays and UV radiation, making ground detection impossible",
      "Because visible light turns into X-rays near the ground",
      "Because ground observatories are only allowed to operate during the day",
      "Because radio waves destroy X-ray telescopes on Earth"],
     "A", "OSC", "easy",
     "Atmospheric molecules (ozone, oxygen, nitrogen) absorb high-energy electromagnetic radiation including X-rays, gamma rays, and far-UV; only visible light and radio waves have open atmospheric transmission windows to reach Earth's surface."),

    # 72: Hubble Space Telescope Ritchey-Chretien Optical Path
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#18181b"/>
  <!-- Telescope Outer Barrel Tube -->
  <rect x="30" y="45" width="340" height="110" rx="6" fill="#0f172a" stroke="#64748b" stroke-width="1.5"/>
  <text x="200" y="38" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Hubble Ritchey-Chrétien Cassegrain Optical Path</text>
  <!-- Primary Mirror (Hyperbolic Concave with Central Hole) -->
  <path d="M 60 50 Q 75 100 60 150" stroke="#facc15" stroke-width="6" fill="none"/>
  <!-- Central Hole in Primary Mirror -->
  <line x1="68" y1="92" x2="68" y2="108" stroke="#0f172a" stroke-width="8"/>
  <text x="50" y="40" fill="#facc15" font-size="7" font-family="sans-serif" text-anchor="middle">Primary (2.4m)</text>
  <!-- Secondary Mirror (Hyperbolic Convex) -->
  <path d="M 320 85 Q 312 100 320 115" stroke="#38bdf8" stroke-width="5" fill="none"/>
  <text x="335" y="75" fill="#38bdf8" font-size="7" font-family="sans-serif" text-anchor="middle">Secondary (0.3m)</text>
  <!-- Incoming Cosmic Starlight -->
  <line x1="360" y1="65" x2="65" y2="65" stroke="#4ade80" stroke-width="2" stroke-dasharray="4"/>
  <line x1="360" y1="135" x2="65" y2="135" stroke="#4ade80" stroke-width="2" stroke-dasharray="4"/>
  <!-- Reflection from Primary to Secondary -->
  <line x1="65" y1="65" x2="315" y2="92" stroke="#4ade80" stroke-width="2"/>
  <line x1="65" y1="135" x2="315" y2="108" stroke="#4ade80" stroke-width="2"/>
  <!-- Reflection from Secondary through Primary Hole to Focal Instruments -->
  <line x1="315" y1="92" x2="30" y2="100" stroke="#f43f5e" stroke-width="2"/>
  <line x1="315" y1="108" x2="30" y2="100" stroke="#f43f5e" stroke-width="2"/>
  <!-- Science Instruments Module behind Primary -->
  <rect x="25" y="85" width="25" height="30" rx="3" fill="#1e3a8a" stroke="#60a5fa" stroke-width="1.5"/>
  <text x="37" y="103" fill="#ffffff" font-size="6" font-family="sans-serif" text-anchor="middle">CCDs</text>
  <!-- Summary Box -->
  <text x="200" y="175" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Hyperbolic Primary & Secondary fold 57.6m focal length into compact 13m tube!</text>
</svg>
</div>
In the optical ray diagram of the Hubble Space Telescope shown above, what path do incoming parallel starlight rays follow to reach the scientific cameras?""",
     ["Rays reflect off the 2.4 m concave primary mirror toward the convex secondary mirror, which reflects them back through a central hole in the primary into the focal plane instruments",
      "Rays pass straight through both mirrors like transparent window glass without bending",
      "Rays reflect backward out the front aperture into deep space",
      "Rays are absorbed by the secondary mirror and converted into heat"],
     "A", "OSC", "easy",
     "The Cassegrain design uses a concave primary mirror to converge starlight onto a convex secondary mirror, which reflects the converging beam through a hole in the primary mirror center to the focal plane instruments, achieving a long focal length in a compact spaceframe."),

    # 73: Chandra Grazing Incidence Mirrors (Wolter Type I)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#090d16"/>
  <!-- Title -->
  <text x="200" y="25" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Chandra Wolter-I Grazing Incidence X-ray Optics</text>
  <!-- Nested Shells (Paraboloid + Hyperboloid) -->
  <!-- Paraboloid Segment (Upper Left) -->
  <path d="M 60 40 L 170 55" stroke="#facc15" stroke-width="4"/>
  <!-- Hyperboloid Segment (Upper Right) -->
  <path d="M 170 55 L 250 80" stroke="#facc15" stroke-width="4"/>
  <!-- Lower Mirror Shell -->
  <path d="M 60 160 L 170 145" stroke="#facc15" stroke-width="4"/>
  <path d="M 170 145 L 250 120" stroke="#facc15" stroke-width="4"/>
  <!-- Labels on Mirrors -->
  <text x="115" y="45" fill="#fef08a" font-size="7" font-family="sans-serif" text-anchor="middle">Paraboloid Shell</text>
  <text x="210" y="65" fill="#fef08a" font-size="7" font-family="sans-serif" text-anchor="middle">Hyperboloid Shell</text>
  <!-- Incoming Grazing X-ray Ray (Top) -->
  <line x1="30" y1="50" x2="140" y2="52" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4"/>
  <!-- Grazing Reflection 1 (Angle < 1 deg) -->
  <line x1="140" y1="52" x2="210" y2="67" stroke="#38bdf8" stroke-width="2"/>
  <!-- Grazing Reflection 2 to Common Focal Point -->
  <line x1="210" y1="67" x2="360" y2="100" stroke="#f43f5e" stroke-width="2"/>
  <!-- Focal Point Detector -->
  <circle cx="360" cy="100" r="6" fill="#ef4444" stroke="#f87171" stroke-width="2"/>
  <text x="360" y="120" fill="#ef4444" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">X-ray Focal Plane (ACIS / HRC)</text>
  <!-- Grazing Angle Note -->
  <text x="140" y="35" fill="#4ade80" font-size="7" font-family="sans-serif">Shallow grazing angle (&lt; 1 deg)</text>
  <!-- Summary Box -->
  <text x="200" y="185" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Like skipping stones on water, high-energy X-rays ricochet off iridium-coated shells!</text>
</svg>
</div>
How does the Wolter-I grazing incidence mirror geometry shown above successfully focus high-energy cosmic X-rays in Chandra?""",
     ["Incoming X-rays strike the interior iridium surfaces at shallow grazing angles (< 1°), ricocheting off parabolic and hyperbolic barrels to converge at a focal detector",
      "X-rays strike normal perpendicular glass mirrors and bounce straight back",
      "X-rays pass through thick acrylic lenses that slow them down",
      "X-rays are magnetically deflected by giant iron electromagnets"],
     "A", "OSC", "medium",
     "Because X-rays penetrate straight into matter at steep angles, Chandra uses nested cylindrical barrel mirrors where X-rays strike at shallow grazing angles (under 1°), ricocheting twice (off paraboloid then hyperboloid surfaces) to focus onto CCD detectors."),

    # 74: Astrosat Multi-Wavelength Payload Stack
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#18181b"/>
  <!-- Satellite Main Bus Box -->
  <rect x="130" y="60" width="140" height="90" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="200" y="80" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">ISRO ASTROSAT BUS</text>
  <!-- Payloads on Top Deck -->
  <!-- UVIT (Left) -->
  <rect x="140" y="25" width="30" height="35" rx="3" fill="#1e3a8a" stroke="#60a5fa" stroke-width="1.5"/>
  <text x="155" y="45" fill="#93c5fd" font-size="7" font-family="sans-serif" text-anchor="middle" font-weight="bold">UVIT</text>
  <!-- SXT (Center-Left) -->
  <rect x="175" y="25" width="25" height="35" rx="3" fill="#14532d" stroke="#4ade80" stroke-width="1.5"/>
  <text x="187" y="45" fill="#4ade80" font-size="7" font-family="sans-serif" text-anchor="middle" font-weight="bold">SXT</text>
  <!-- LAXPC (Center-Right) -->
  <rect x="205" y="20" width="35" height="40" rx="3" fill="#78350f" stroke="#facc15" stroke-width="1.5"/>
  <text x="222" y="45" fill="#facc15" font-size="7" font-family="sans-serif" text-anchor="middle" font-weight="bold">LAXPC</text>
  <!-- CZTI (Right) -->
  <rect x="245" y="25" width="20" height="35" rx="3" fill="#450a0a" stroke="#ef4444" stroke-width="1.5"/>
  <text x="255" y="45" fill="#ef4444" font-size="6" font-family="sans-serif" text-anchor="middle" font-weight="bold">CZTI</text>
  <!-- Solar Panels Flanking Bus -->
  <rect x="20" y="85" width="105" height="40" rx="3" fill="#0284c7" stroke="#38bdf8" stroke-width="1"/>
  <line x1="55" y1="85" x2="55" y2="125" stroke="#0369a1" stroke-width="1"/>
  <line x1="90" y1="85" x2="90" y2="125" stroke="#0369a1" stroke-width="1"/>
  <text x="72" y="108" fill="#ffffff" font-size="7" font-family="sans-serif" text-anchor="middle">Solar Array</text>
  <rect x="275" y="85" width="105" height="40" rx="3" fill="#0284c7" stroke="#38bdf8" stroke-width="1"/>
  <line x1="310" y1="85" x2="310" y2="125" stroke="#0369a1" stroke-width="1"/>
  <line x1="345" y1="85" x2="345" y2="125" stroke="#0369a1" stroke-width="1"/>
  <text x="327" y="108" fill="#ffffff" font-size="7" font-family="sans-serif" text-anchor="middle">Solar Array</text>
  <!-- Spectrum Band Legend -->
  <text x="200" y="165" fill="#cbd5e1" font-size="7" font-family="sans-serif" text-anchor="middle">Simultaneous Coverage: UV (UVIT), Soft X-rays (SXT), Hard X-rays (LAXPC, CZTI)</text>
  <text x="200" y="182" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Multi-wavelength synchronization reveals complete high-energy astrophysics!</text>
</svg>
</div>
What makes the co-aligned payload architecture of India's Astrosat uniquely valuable for studying cosmic high-energy sources?""",
     ["It observes the same celestial source simultaneously across Optical, Ultraviolet, Soft X-ray, and Hard X-ray wavelengths without time lag",
      "It allows astronauts to steer the satellite using a steering wheel",
      "It generates free electricity and beams it to Earth",
      "It repairs broken satellites in geostationary orbit"],
     "A", "OSC", "easy",
     "Astrosat's co-aligned payloads (UVIT, SXT, LAXPC, CZTI) observe targets concurrently; this eliminates calibration mismatches and timing delays when tracking rapidly flaring black hole and neutron star binary systems across the electromagnetic spectrum."),

    # 75: Chandrayaan-1 Moon Impact Probe (MIP) & Water Discovery
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#090d16"/>
  <!-- Chandrayaan-1 Orbiter (Top Left) -->
  <rect x="30" y="30" width="60" height="40" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="60" y="55" fill="#38bdf8" font-size="7" font-family="sans-serif" text-anchor="middle" font-weight="bold">Chandrayaan-1</text>
  <text x="60" y="65" fill="#cbd5e1" font-size="6" font-family="sans-serif" text-anchor="middle">100 km Orbit</text>
  <!-- Separation Trajectory of MIP -->
  <path d="M 90 50 Q 200 60 260 140" stroke="#facc15" stroke-width="2" stroke-dasharray="4" fill="none"/>
  <!-- MIP Box in Flight -->
  <rect x="175" y="75" width="25" height="20" rx="2" fill="#78350f" stroke="#facc15" stroke-width="1.5"/>
  <text x="187" y="88" fill="#facc15" font-size="6" font-family="sans-serif" text-anchor="middle" font-weight="bold">MIP</text>
  <!-- Moon Surface with Craters (Bottom) -->
  <path d="M 20 170 Q 150 145 280 150 Q 340 160 380 170" stroke="#94a3b8" stroke-width="3" fill="#334155"/>
  <!-- Shackleton Crater at South Pole -->
  <ellipse cx="280" cy="150" rx="25" ry="10" fill="#0f172a" stroke="#64748b" stroke-width="1.5"/>
  <text x="280" y="175" fill="#fca5a5" font-size="7" font-family="sans-serif" text-anchor="middle" font-weight="bold">South Pole (Shackleton)</text>
  <!-- Diagnostic Absorption 2.8 - 3.0 um signature -->
  <rect x="250" y="25" width="130" height="55" rx="4" fill="#18181b" stroke="#4ade80" stroke-width="1"/>
  <text x="315" y="40" fill="#4ade80" font-size="7" font-family="sans-serif" text-anchor="middle" font-weight="bold">M3 Diagnostic Signature</text>
  <path d="M 260 60 Q 285 60 295 72 Q 305 60 330 60" stroke="#4ade80" stroke-width="1.5" fill="none"/>
  <text x="315" y="74" fill="#facc15" font-size="6" font-family="sans-serif" text-anchor="middle">H2O / OH Absorption (3.0 um)</text>
  <!-- Summary Box -->
  <text x="200" y="192" fill="#38bdf8" font-size="7" font-family="sans-serif" text-anchor="middle">Historic Discovery: Chandrayaan-1 proved water molecules exist on the lunar surface!</text>
</svg>
</div>
What dual breakthrough discovery did India's Chandrayaan-1 mission achieve regarding lunar water in 2008?""",
     ["The Moon Impact Probe (CHACE) directly sampled water vapor during its descent, while NASA's M3 spectrometer confirmed hydroxyl/water absorption bands in polar soil",
      "It discovered flowing hot rivers and active geysers on the lunar equator",
      "It found frozen icebergs floating in lunar oceans",
      "It proved the Moon is completely made of dry volcanic glass with zero hydrogen"],
     "A", "OSC", "easy",
     "Chandrayaan-1 provided definitive proof of lunar water: the Indian Moon Impact Probe's mass spectrometer directly detected water molecules in the thin lunar exosphere, and the M3 spectrometer recorded distinct 2.8–3.0 µm infrared absorption bands of H2O and OH in polar regolith."),

    # 76: Mangalyaan (Mars Orbiter Mission) Hohmann Transfer Orbit
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#090d16"/>
  <!-- Central Sun -->
  <circle cx="160" cy="100" r="14" fill="#facc15" stroke="#f59e0b" stroke-width="2"/>
  <text x="160" y="103" fill="#78350f" font-size="6" font-family="sans-serif" text-anchor="middle" font-weight="bold">Sun</text>
  <!-- Earth Orbit (Blue inner circle) -->
  <circle cx="160" cy="100" r="45" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3"/>
  <!-- Earth at Launch Point -->
  <circle cx="160" cy="55" r="5" fill="#0284c7"/>
  <text x="160" y="47" fill="#38bdf8" font-size="7" font-family="sans-serif" text-anchor="middle" font-weight="bold">Earth Departure (Nov 2013)</text>
  <!-- Mars Orbit (Red outer circle) -->
  <circle cx="160" cy="100" r="85" fill="none" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3"/>
  <!-- Mars at Insertion Point -->
  <circle cx="160" cy="185" r="4" fill="#ef4444"/>
  <text x="160" y="196" fill="#f87171" font-size="7" font-family="sans-serif" text-anchor="middle" font-weight="bold">Mars Orbit Insertion (24 Sep 2014)</text>
  <!-- Hohmann Transfer Ellipse (Green Curve) -->
  <path d="M 160 55 A 50 65 0 0 1 160 185" stroke="#4ade80" stroke-width="2.5" fill="none"/>
  <!-- Direction Arrow along Ellipse -->
  <polygon points="215,115 220,123 210,123" fill="#4ade80" transform="rotate(30, 215, 115)"/>
  <!-- Mangalyaan Box Label -->
  <rect x="245" y="30" width="135" height="60" rx="4" fill="#18181b" stroke="#4ade80" stroke-width="1"/>
  <text x="312" y="46" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Hohmann Transfer Trajectory</text>
  <text x="312" y="60" fill="#cbd5e1" font-size="7" font-family="sans-serif" text-anchor="middle">Distance: ~660 Million km</text>
  <text x="312" y="73" fill="#facc15" font-size="7" font-family="sans-serif" text-anchor="middle">Travel Time: 300 Days</text>
  <text x="312" y="84" fill="#86efac" font-size="6" font-family="sans-serif" text-anchor="middle">Success on maiden attempt!</text>
</svg>
</div>
How did ISRO's Mangalyaan navigate across 660 million kilometers of space to enter Martian orbit on its maiden attempt?""",
     ["It followed a minimum-energy heliocentric Hohmann transfer ellipse, with perihelion at Earth's orbit and aphelion at Mars' orbit, executing a precise deceleration burn at arrival",
      "It flew in a straight line directly from Earth to Mars like a bullet",
      "It circled the Moon ten times until Mars pulled it into orbit",
      "It relied on Martian astronauts sending remote radio controls"],
     "A", "OSC", "medium",
     "Mangalyaan utilized a classic Hohmann transfer ellipse: after Earth-escape burn, the spacecraft coasted around the Sun along an elliptical orbit for ~300 days until intersecting Mars, where a 24-minute burn of its 440 N engine captured it into Martian orbit."),

    # 77: Chandrayaan-3 Vikram Soft Landing & Pragyan Rover Deployment
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#090d16"/>
  <!-- Lunar Ground Surface -->
  <rect x="20" y="145" width="360" height="45" fill="#334155" stroke="#64748b" stroke-width="1.5" rx="3"/>
  <text x="200" y="165" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Lunar South Pole Regolith (Shiv Shakti Point - 69.37° S)</text>
  <text x="200" y="180" fill="#4ade80" font-size="7" font-family="sans-serif" text-anchor="middle">Touchdown: 23 August 2023 at 18:04 IST</text>
  <!-- Vikram Lander Body -->
  <rect x="80" y="70" width="70" height="55" rx="4" fill="#1e293b" stroke="#facc15" stroke-width="2"/>
  <text x="115" y="95" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">VIKRAM</text>
  <text x="115" y="108" fill="#cbd5e1" font-size="7" font-family="sans-serif" text-anchor="middle">Lander</text>
  <!-- Lander Legs -->
  <line x1="85" y1="125" x2="70" y2="145" stroke="#facc15" stroke-width="3"/>
  <line x1="145" y1="125" x2="160" y2="145" stroke="#facc15" stroke-width="3"/>
  <!-- Deployment Ramp -->
  <line x1="150" y1="110" x2="220" y2="145" stroke="#38bdf8" stroke-width="3"/>
  <!-- Pragyan Rover Rolling on Ramp/Surface -->
  <rect x="220" y="125" width="45" height="20" rx="2" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="242" y="137" fill="#ffffff" font-size="7" font-family="sans-serif" text-anchor="middle" font-weight="bold">PRAGYAN</text>
  <!-- Rover Wheels (6 Wheels) -->
  <circle cx="225" cy="145" r="3" fill="#facc15"/>
  <circle cx="233" cy="145" r="3" fill="#facc15"/>
  <circle cx="242" cy="145" r="3" fill="#facc15"/>
  <circle cx="250" cy="145" r="3" fill="#facc15"/>
  <circle cx="258" cy="145" r="3" fill="#facc15"/>
  <!-- Scientific Payloads Callouts -->
  <rect x="280" y="40" width="105" height="70" rx="4" fill="#18181b" stroke="#4ade80" stroke-width="1"/>
  <text x="332" y="55" fill="#4ade80" font-size="7" font-family="sans-serif" text-anchor="middle" font-weight="bold">Key Scientific Payloads:</text>
  <text x="332" y="70" fill="#facc15" font-size="6" font-family="sans-serif" text-anchor="middle">ChaSTE (Thermal Gradient)</text>
  <text x="332" y="82" fill="#38bdf8" font-size="6" font-family="sans-serif" text-anchor="middle">ILSA (Lunar Seismicity)</text>
  <text x="332" y="94" fill="#f87171" font-size="6" font-family="sans-serif" text-anchor="middle">LIBS (Sulfur detection)</text>
</svg>
</div>
What key scientific payloads operated on the Vikram lander and Pragyan rover to investigate the Moon's south polar regolith?""",
     ["ChaSTE measured regolith thermal conductivity, ILSA recorded lunar moonquakes, and LIBS confirmed the presence of elemental Sulfur",
      "A telescope to watch Earth television, a radio to play songs, and a camera for selfies",
      "A water drill to pump water into tanks and a heater to melt glaciers",
      "A radar to search for alien bunkers under the craters"],
     "A", "OSC", "easy",
     "Vikram carried ChaSTE (thermal probe), ILSA (seismometer), and RAMBHA-LP (plasma probe); the Pragyan rover carried LIBS (laser-induced breakdown spectroscopy) which unambiguously identified elemental Sulfur and minerals in the lunar soil."),

    # 78: Aditya-L1 Halo Orbit at Lagrange Point 1
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#090d16"/>
  <!-- The Sun (Left) -->
  <circle cx="40" cy="100" r="30" fill="#f59e0b" stroke="#facc15" stroke-width="2"/>
  <text x="40" y="104" fill="#78350f" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">SUN</text>
  <!-- Solar Radiation / Wind Stream -->
  <line x1="75" y1="100" x2="330" y2="100" stroke="#fef08a" stroke-width="1.5" stroke-dasharray="3"/>
  <!-- Lagrange Point 1 Halo Orbit (Center-Right) -->
  <ellipse cx="230" cy="100" rx="20" ry="45" fill="none" stroke="#4ade80" stroke-width="2" stroke-dasharray="4"/>
  <circle cx="230" cy="65" r="5" fill="#38bdf8"/>
  <text x="230" y="55" fill="#38bdf8" font-size="7" font-family="sans-serif" text-anchor="middle" font-weight="bold">Aditya-L1 Spacecraft</text>
  <text x="230" y="160" fill="#4ade80" font-size="7" font-family="sans-serif" text-anchor="middle" font-weight="bold">Halo Orbit at L1</text>
  <!-- Earth (Right) -->
  <circle cx="350" cy="100" r="14" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="350" y="103" fill="#ffffff" font-size="7" font-family="sans-serif" text-anchor="middle" font-weight="bold">Earth</text>
  <!-- Distance Callout -->
  <line x1="230" y1="120" x2="350" y2="120" stroke="#facc15" stroke-width="1"/>
  <text x="290" y="132" fill="#facc15" font-size="7" font-family="sans-serif" text-anchor="middle">1.5 Million km</text>
  <text x="290" y="142" fill="#cbd5e1" font-size="6" font-family="sans-serif" text-anchor="middle">(1% Sun-Earth distance)</text>
  <!-- Summary Box -->
  <text x="200" y="190" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Zero Occultation: Unbroken 24/7 view of the solar corona, solar wind, and flares!</text>
</svg>
</div>
Why did ISRO place Aditya-L1 into a halo orbit around the Sun-Earth Lagrange Point 1 (L1) rather than a low Earth orbit?""",
     ["At L1, the spacecraft enjoys an uninterrupted 24/7 view of the Sun without any eclipses or occultation by Earth or Moon, while sampling pristine solar wind",
      "Because low Earth orbit is too cold for solar instruments",
      "Because Earth's gravity stops working at Lagrange Point 1",
      "To allow the spacecraft to land on the Moon during weekends"],
     "A", "OSC", "easy",
     "Lagrange Point 1 is an equilibrium point where gravitational forces of Earth and Sun balance spacecraft orbital motion; orbiting L1 in a halo orbit ensures the Sun is never eclipsed by Earth, providing uninterrupted solar observations and in-situ space weather monitoring."),

    # 79: ISRO Launch Vehicle Evolution (SLV-3 to LVM3)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#18181b"/>
  <!-- Title -->
  <text x="200" y="25" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Evolution of Indian Launch Vehicles: 40 kg to 4,000 kg Payload</text>
  <!-- 1. SLV-3 (1980) -->
  <rect x="35" y="110" width="12" height="45" fill="#94a3b8" rx="2"/>
  <polygon points="41,95 35,110 47,110" fill="#ef4444"/>
  <text x="41" y="170" fill="#cbd5e1" font-size="7" font-family="sans-serif" text-anchor="middle">SLV-3</text>
  <text x="41" y="180" fill="#facc15" font-size="6" font-family="sans-serif" text-anchor="middle">40 kg LEO</text>
  <!-- 2. ASLV (1987) -->
  <rect x="95" y="100" width="16" height="55" fill="#94a3b8" rx="2"/>
  <polygon points="103,85 95,100 111,100" fill="#ef4444"/>
  <text x="103" y="170" fill="#cbd5e1" font-size="7" font-family="sans-serif" text-anchor="middle">ASLV</text>
  <text x="103" y="180" fill="#facc15" font-size="6" font-family="sans-serif" text-anchor="middle">150 kg</text>
  <!-- 3. PSLV (1993 - Workhorse) -->
  <rect x="180" y="70" width="22" height="85" fill="#38bdf8" rx="3"/>
  <polygon points="191,55 180,70 202,70" fill="#f43f5e"/>
  <text x="191" y="170" fill="#38bdf8" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">PSLV</text>
  <text x="191" y="180" fill="#4ade80" font-size="6" font-family="sans-serif" text-anchor="middle">1750 kg SSO</text>
  <!-- 4. LVM3 (Heavy Lifter) -->
  <rect x="300" y="50" width="35" height="105" fill="#1e3a8a" stroke="#60a5fa" stroke-width="1.5" rx="4"/>
  <polygon points="317,35 300,50 335,50" fill="#ef4444"/>
  <!-- Twin S200 Boosters -->
  <rect x="286" y="75" width="12" height="75" fill="#f59e0b" rx="2"/>
  <rect x="337" y="75" width="12" height="75" fill="#f59e0b" rx="2"/>
  <text x="317" y="170" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">LVM3</text>
  <text x="317" y="180" fill="#4ade80" font-size="6" font-family="sans-serif" text-anchor="middle">4000 kg GTO</text>
</svg>
</div>
How did India's rocket lifting capability evolve from the historic SLV-3 (1980) to the modern heavy-lifter LVM3 (2023)?""",
     ["Payload capacity expanded by 100-fold, growing from 40 kg into low Earth orbit to 4,000 kg into geostationary transfer orbit with indigenous cryogenic upper stages",
      "Lifting capacity decreased because modern satellites are made of paper",
      "India discontinued all rockets and uses aeroplanes to carry satellites",
      "Rockets were replaced by long ropes anchored to the Moon"],
     "A", "OSC", "easy",
     "From SLV-3 in 1980 which placed 40 kg Rohini into orbit, ISRO progressively developed ASLV, PSLV (1.75 tonnes to SSO), GSLV, and LVM3 (4 tonnes to GTO / 8 tonnes to LEO), mastering solid, liquid, and indigenous cryogenic rocketry."),

    # 80: Geosynchronous (GEO) vs Polar Sun-Synchronous (SSO) Orbits
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#090d16"/>
  <!-- Central Earth -->
  <circle cx="200" cy="100" r="30" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="200" y="103" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Earth</text>
  <!-- Geostationary Orbit (Equatorial - Huge Circle) -->
  <ellipse cx="200" cy="100" rx="170" ry="40" fill="none" stroke="#facc15" stroke-width="2"/>
  <circle cx="370" cy="100" r="5" fill="#facc15"/>
  <text x="300" y="80" fill="#facc15" font-size="7" font-family="sans-serif" font-weight="bold">GEO: 36,000 km</text>
  <text x="300" y="90" fill="#cbd5e1" font-size="6" font-family="sans-serif">Period = 24h (INSAT/GSAT)</text>
  <!-- Polar Sun-Synchronous Orbit (Vertical Orbit) -->
  <ellipse cx="200" cy="100" rx="38" ry="85" fill="none" stroke="#4ade80" stroke-width="2" stroke-dasharray="3"/>
  <circle cx="200" cy="15" r="4" fill="#4ade80"/>
  <text x="200" y="10" fill="#4ade80" font-size="7" font-family="sans-serif" text-anchor="middle" font-weight="bold">SSO: 600-800 km</text>
  <text x="140" y="150" fill="#86efac" font-size="6" font-family="sans-serif">Period ~ 95 min (IRS Series)</text>
  <!-- Summary Box -->
  <text x="200" y="190" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">GEO remains fixed over one spot for communications; SSO sweeps the whole planet for Earth observation!</text>
</svg>
</div>
Why does ISRO utilize both Geostationary (GEO) and Sun-Synchronous Polar (SSO) orbits for its national satellite constellations?""",
     ["GEO matches Earth's rotation to stay permanently over India for uninterrupted communications, while SSO orbits over the poles to map Earth's entire surface under consistent daylight",
      "GEO is only used when the Sun is shining, while SSO is only used during night",
      "Because SSO satellites run out of fuel every week",
      "Because GEO is inside the ocean and SSO is in the clouds"],
     "A", "OSC", "easy",
     "Geostationary satellites (INSAT/GSAT) circle at 36,000 km in 24 hours, remaining fixed over India for constant TV, telecom, and weather monitoring; Sun-synchronous satellites (IRS) circle near the poles at 700 km, scanning the entire globe under uniform sun lighting for agriculture and cartography."),

    # 81: Reaction Wheel Attitude Control Principle
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#18181b"/>
  <!-- Spacecraft Main Frame -->
  <rect x="70" y="40" width="260" height="120" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="200" y="60" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Spacecraft Attitude Control via Conservation of Angular Momentum</text>
  <!-- Reaction Wheel (Flywheel inside) -->
  <circle cx="200" cy="105" r="30" fill="#0f172a" stroke="#facc15" stroke-width="2.5"/>
  <circle cx="200" cy="105" r="8" fill="#f59e0b"/>
  <text x="200" y="102" fill="#facc15" font-size="7" font-family="sans-serif" text-anchor="middle" font-weight="bold">Internal</text>
  <text x="200" y="112" fill="#facc15" font-size="7" font-family="sans-serif" text-anchor="middle" font-weight="bold">Flywheel</text>
  <!-- Wheel Spin Clockwise Arrow -->
  <path d="M 180 80 A 25 25 0 0 1 220 80" stroke="#facc15" stroke-width="2.5" fill="none"/>
  <polygon points="220,80 216,74 213,82" fill="#facc15"/>
  <text x="200" y="75" fill="#facc15" font-size="7" font-family="sans-serif" text-anchor="middle">Flywheel Spun Clockwise (+L)</text>
  <!-- Spacecraft Counter-Rotation Arrow (Counter-Clockwise) -->
  <path d="M 120 150 A 90 90 0 0 1 280 150" stroke="#4ade80" stroke-width="2.5" fill="none"/>
  <polygon points="120,150 125,155 125,145" fill="#4ade80"/>
  <text x="200" y="145" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Spacecraft Body Rotates Counter-Clockwise (-L)</text>
  <!-- Takeaway Formula -->
  <text x="200" y="180" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">L_total = I_wheel * omega_wheel + I_body * omega_body = Constant (Zero Propellant Used!)</text>
</svg>
</div>
How does a space telescope steer itself with arcsecond precision in the vacuum of space without using any rocket propellant?""",
     ["By electrically accelerating internal flywheels (reaction wheels), inducing an equal and opposite counter-rotation in the spacecraft body via Conservation of Angular Momentum",
      "By opening parachute flaps to catch space breezes",
      "By firing fireworks out of the sides of the telescope tube",
      "By using oars to paddle through dark matter"],
     "A", "OSC", "easy",
     "In the frictionless vacuum of orbit, total angular momentum is strictly conserved; spinning an internal flywheel in one direction exerts a reaction torque that rotates the entire spacecraft in the opposite direction, allowing exact pinpoint reorientation without burning thruster propellant."),

    # 82: Global Impact of Indian Space Technology
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#090d16"/>
  <!-- Central Shield / Emblem -->
  <circle cx="200" cy="100" r="45" fill="#1e3a8a" stroke="#facc15" stroke-width="2"/>
  <text x="200" y="95" fill="#facc15" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">ISRO</text>
  <text x="200" y="112" fill="#38bdf8" font-size="8" font-family="sans-serif" text-anchor="middle">Est. 1969</text>
  <!-- Surrounding Application Pillars -->
  <!-- 1. Mass Education (EDUSAT) -->
  <rect x="25" y="25" width="105" height="45" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="77" y="42" fill="#38bdf8" font-size="7" font-family="sans-serif" text-anchor="middle" font-weight="bold">EDUCATION</text>
  <text x="77" y="55" fill="#cbd5e1" font-size="6" font-family="sans-serif" text-anchor="middle">EDUSAT tele-classrooms</text>
  <!-- 2. Weather & Disaster Management -->
  <rect x="270" y="25" width="105" height="45" rx="4" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
  <text x="322" y="42" fill="#ef4444" font-size="7" font-family="sans-serif" text-anchor="middle" font-weight="bold">DISASTER RELIEF</text>
  <text x="322" y="55" fill="#cbd5e1" font-size="6" font-family="sans-serif" text-anchor="middle">Cyclone early warnings</text>
  <!-- 3. Navigation & Defense (NavIC) -->
  <rect x="25" y="130" width="105" height="45" rx="4" fill="#1e293b" stroke="#4ade80" stroke-width="1.5"/>
  <text x="77" y="148" fill="#4ade80" font-size="7" font-family="sans-serif" text-anchor="middle" font-weight="bold">NAVIGATION</text>
  <text x="77" y="160" fill="#cbd5e1" font-size="6" font-family="sans-serif" text-anchor="middle">NavIC positioning</text>
  <!-- 4. Deep Space Exploration -->
  <rect x="270" y="130" width="105" height="45" rx="4" fill="#1e293b" stroke="#facc15" stroke-width="1.5"/>
  <text x="322" y="148" fill="#facc15" font-size="7" font-family="sans-serif" text-anchor="middle" font-weight="bold">DEEP SPACE</text>
  <text x="322" y="160" fill="#cbd5e1" font-size="6" font-family="sans-serif" text-anchor="middle">Chandrayaan & Mangalyaan</text>
  <!-- Connecting Lines -->
  <line x1="130" y1="47" x2="165" y2="75" stroke="#64748b" stroke-width="1.5"/>
  <line x1="270" y1="47" x2="235" y2="75" stroke="#64748b" stroke-width="1.5"/>
  <line x1="130" y1="152" x2="165" y2="125" stroke="#64748b" stroke-width="1.5"/>
  <line x1="270" y1="152" x2="235" y2="125" stroke="#64748b" stroke-width="1.5"/>
  <!-- Footer Note -->
  <text x="200" y="190" fill="#cbd5e1" font-size="7" font-family="sans-serif" text-anchor="middle">Dr. Vikram Sarabhai's vision: Space technology directly serving human society!</text>
</svg>
</div>
How does ISRO's philosophy of space exploration fundamentally embody Dr. Vikram Sarabhai's founding vision?""",
     ["Space technology is developed not for prestige, but as an indispensable tool for national development—improving tele-education, cyclone disaster warning, tele-medicine, agriculture, and high-frontier science",
      "Space technology was developed solely to win foreign trophies and medals",
      "Space technology was built to replace all teachers and schools with machines",
      "Space technology was intended to build luxury hotels on the Moon"],
     "A", "OSC", "easy",
     "Dr. Vikram Sarabhai declared that India must be second to none in the application of advanced technologies to the real problems of society; ISRO's programmes directly empower tele-education, weather forecasting, crop monitoring, tele-medicine, and sovereign navigation while leading world-class planetary science.")
]

all_questions = []

# Exam: 40 questions (1-40)
for idx, item in enumerate(exam_data):
    qnum = idx + 1
    qcode = f"{TOPIC_CODE}-{item[3]}-{qnum:03d}"
    all_questions.append(
        make_q(qcode, TOPIC_CODE, item[0], item[1], item[2], item[3], item[4], "exam", "standard", item[5])
    )

# Practice: 30 questions (41-70)
for idx, item in enumerate(practice_data):
    qnum = idx + 41
    qcode = f"{TOPIC_CODE}-{item[3]}-{qnum:03d}"
    all_questions.append(
        make_q(qcode, TOPIC_CODE, item[0], item[1], item[2], item[3], item[4], "practice", "standard", item[5])
    )

# Mock: 12 questions (71-82)
for idx, item in enumerate(mock_data):
    qnum = idx + 71
    qcode = f"{TOPIC_CODE}-{item[3]}-{qnum:03d}"
    all_questions.append(
        make_q(qcode, TOPIC_CODE, item[0], item[1], item[2], item[3], item[4], "mock", "foundation", item[5])
    )

print(f"Generated {len(all_questions)} questions for {TOPIC_CODE}")

output_path = os.path.join(os.path.dirname(__file__), "ch18_topic4.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Saved to {output_path}")
