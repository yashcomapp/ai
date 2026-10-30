# scripts/generate_ch12_topic2.py
# MH-9-SCIT-12-12.2: Audible, Infrasonic and Ultrasonic Sound
import json
import sys
import os

sys.path.append(os.path.dirname(__file__))
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-12-12.2"

exam_data = [
    # 1-10: Frequency Ranges & Audible Limits
    ("What is the standard frequency range of audible sound for a healthy human ear?",
     ["20 Hz to 20,000 Hz (20 Hz to 20 kHz)",
      "0 Hz to 100 Hz",
      "20 kHz to 100 kHz",
      "1 Hz to 500 Hz"],
     "A", "OSC", "easy",
     "The normal audible acoustic frequency range for human ears spans from approximately 20 Hz at the low end to 20,000 Hz (20 kHz) at the high end."),

    ("What are sound waves with frequencies strictly below 20 Hz called?",
     ["Infrasonic sound (infrasound)",
      "Ultrasonic sound (ultrasound)",
      "Audible acoustic waves",
      "Supersonic waves"],
     "A", "OSC", "easy",
     "Sound waves whose vibrational frequencies lie below the threshold of human audibility (under 20 Hz) are termed infrasound or infrasonic waves."),

    ("What are sound waves with frequencies strictly above 20,000 Hz (20 kHz) called?",
     ["Ultrasonic sound (ultrasound)",
      "Infrasonic sound (infrasound)",
      "Subsonic waves",
      "Audible harmonics"],
     "A", "OSC", "easy",
     "Acoustic frequencies exceeding the upper limit of human hearing (greater than 20,000 Hz) are known as ultrasound or ultrasonic waves."),

    ("Which of the following animals communicates over long distances using low-frequency infrasound as low as 5 Hz to 15 Hz?",
     ["Rhinoceroses, elephants, and blue whales",
      "Bats and dolphins",
      "Dogs and mice",
      "Honeybees and houseflies"],
     "A", "OSC", "easy",
     "Rhinoceroses (communicating at ~5 Hz), elephants (14-16 Hz), and large whales generate deep infrasound that travels for kilometers through ground and ocean waters without rapid absorption."),

    ("What natural geophysical disaster is preceded by low-frequency infrasonic vibrations that alert animals before the main shockwaves arrive?",
     ["Earthquakes and volcanic eruptions",
      "Solar flares",
      "Aurora borealis",
      "Thunderstorm lightning flashes"],
     "A", "OSC", "easy",
     "Tectonic crustal stress fractures produce low-frequency infrasound before the destructive secondary seismic waves arrive, causing animals like dogs, birds, and snakes to act agitated."),

    ("Which flying mammal uses high-frequency ultrasonic echolocation clicks (up to 100 kHz) to navigate and hunt flying insects in pitch darkness?",
     ["Bats", "Owls", "Eagles", "Flying squirrels"],
     "A", "OSC", "easy",
     "Bats emit ultrasonic squeaks and pulses through their mouth or nose; by detecting the reflected echo timing and direction, they form a detailed 3D acoustic map of obstacles and prey."),

    ("Which aquatic mammal navigates murky waters and communicates with its pod using ultrasonic clicks and whistles?",
     ["Dolphins and porpoises", "Jellyfish", "Sharks", "Sea cucumbers"],
     "A", "OSC", "easy",
     "Dolphins produce ultrasonic clicks up to 150 kHz, using melon acoustic lensing for echolocation to identify fish species and underwater terrain."),

    ("What specialized acoustic whistle produces high-frequency ultrasound (around 25 kHz to 40 kHz) that dogs can hear but humans cannot?",
     ["Galton's whistle (silent dog whistle)",
      "Police referee whistle",
      "Steam siren",
      "Doppler whistle"],
     "A", "OSC", "easy",
     "Invented by Francis Galton, a Galton whistle produces acoustic tones above 20 kHz, which lie within the broader hearing range of canines (~45-50 kHz) while remaining silent to human ears."),

    ("How high can the hearing frequency range of young domestic cats and dogs extend?",
     ["Up to 45 kHz to 64 kHz",
      "Up to only 15 kHz",
      "Up to 500 kHz",
      "Limited strictly to 20 kHz like humans"],
     "A", "OSC", "easy",
     "Dogs can hear up to ~45-50 kHz, and cats can perceive ultrasonic frequencies up to ~64 kHz, enabling them to detect the faint high-pitched rustling of rodents."),

    ("What is the difference between 'ultrasonic' and 'supersonic' in physics?",
     ["Ultrasonic refers to sound frequencies above 20 kHz; Supersonic refers to physical objects moving at speeds greater than the speed of sound",
      "Ultrasonic means moving faster than light; Supersonic means moving slower than sound",
      "Both terms mean exactly the same thing",
      "Ultrasonic is a type of laser; Supersonic is a type of radar"],
     "A", "OSC", "medium",
     "Ultrasonic describes wave frequency (> 20 kHz), while supersonic describes mechanical speed exceeding Mach 1 (speed of sound in the surrounding medium, ~340 m/s in air)."),

    # 11-20: Industrial & Medical Applications of Ultrasound
    ("How is high-frequency ultrasound utilized in industrial ultrasonic cleaning baths?",
     ["Ultrasonic vibrations create millions of microscopic cavitation bubbles in a liquid cleaner that implode violently, dislodging dirt and grease from intricate parts",
      "The sound waves heat the metal to melting point",
      "The sound dissolves metal parts completely",
      "Sound waves coat parts with protective paint"],
     "A", "OSC", "medium",
     "Ultrasonic transducers generate intense pressure waves that cause acoustic cavitation. Microscopic bubbles violently collapse against components, scrubbing dirt, grease, and oxide off watch parts, circuit boards, and jewelry without mechanical abrasion."),

    ("How is ultrasound used to detect hidden internal cracks, porosity, and voids in heavy steel blocks without breaking them?",
     ["Ultrasound pulses are transmitted through the block; if a crack is present, part of the wave reflects early back to the detector",
      "The ultrasound heats the crack until it glows red",
      "The sound magnetic forces re-weld the crack",
      "Ultrasound turns the steel transparent"],
     "A", "OSC", "easy",
     "In non-destructive flaw detection (NDT), ultrasonic waves travel cleanly through homogeneous metal; any interior defect, crack, or air void reflects a fraction of the pulse back early, signaling the defect's exact depth."),

    ("What medical diagnostic technique uses high-frequency ultrasound (2 MHz to 10 MHz) to visualize internal soft organs like the liver, kidneys, and uterus?",
     ["Ultrasonography (medical sonography / ultrasound scan)",
      "Magnetic Resonance Imaging (MRI)",
      "Computed Tomography (CT scan)",
      "X-ray radiography"],
     "A", "OSC", "easy",
     "Medical ultrasonography transmits painless high-frequency sound pulses into the human body. As waves encounter boundaries between tissues of differing acoustic impedance, echoes reflect back to build real-time anatomical images."),

    ("Why is ultrasonography considered much safer than traditional X-rays for monitoring the development of a human fetus during pregnancy?",
     ["Ultrasound consists of non-ionizing mechanical acoustic waves that cause no cellular radiation damage or genetic mutations",
      "Ultrasound produces visible light instead of radiation",
      "Ultrasound freezes the fetus in place",
      "X-rays are made of hot sound waves"],
     "A", "OSC", "easy",
     "Unlike ionizing X-rays that can mutate fetal DNA and induce developmental birth defects, diagnostic ultrasound uses low-power mechanical pressure waves that are biologically safe."),

    ("What specialized ultrasound imaging technique examines the structure and rhythmic motion of the heart valves and cardiac muscle chambers?",
     ["Echocardiography (ECHO)",
      "Electroencephalography (EEG)",
      "Angiography",
      "Endoscopy"],
     "A", "OSC", "easy",
     "Echocardiography employs ultrasonic transducers placed on the chest to monitor real-time pumping of cardiac chambers, opening/closing of heart valves, and blood regurgitation."),

    ("Which medical procedure uses high-intensity focused ultrasound (HIFU) shockwaves to pulverize kidney stones into fine gravel passed in urine?",
     ["Extracorporeal Shock Wave Lithotripsy (ESWL)",
      "Dialysis filtration",
      "Chemotherapy",
      "Electroconvulsive therapy"],
     "A", "OSC", "easy",
     "In lithotripsy, focused acoustic shockwaves pass safely through soft flesh and converge on kidney stones, shattering the brittle calcium deposits into tiny sand-sized grains without open surgery."),

    ("How is ultrasound utilized in dairy food processing and homogenisation?",
     ["Ultrasound disrupts and disperses fat globules into uniform sub-micron emulsions and ruptures bacterial cell membranes",
      "It freezes milk instantly into powder",
      "It removes lactose completely",
      "It adds synthetic calcium vitamins"],
     "A", "OSC", "easy",
     "Acoustic cavitation physically shears large milk fat globules into a permanently dispersed colloidal emulsion and lyses vegetative spoilage bacteria, extending milk shelf-life."),

    ("Why cannot human ears perceive ultrasonic waves emitted by bats or medical ultrasound probes?",
     ["The frequency is higher than the mechanical resonant capability of the human eardrum and inner ear basilar membrane (above 20,000 Hz)",
      "Because ultrasonic waves travel at the speed of light",
      "Because ultrasound waves have zero energy",
      "Because human ears can only hear sound in water"],
     "A", "OSC", "easy",
     "The physical mass and elasticity of the human tympanic membrane and cochlear hair cells cannot vibrate at frequencies exceeding ~20 kHz, setting the biological limit of audibility."),

    ("What type of insect has evolved specialized ultrasound-sensitive ears on its abdomen or thorax to hear the echolocation calls of hunting bats and evade capture?",
     ["Certain nocturnal moths (tiger moths)",
      "Houseflies",
      "Earthworms",
      "Garden snails"],
     "A", "OSC", "medium",
     "Certain nocturnal moths possess tympanal organs tuned specifically to 20-80 kHz bat echolocation frequencies, allowing them to perform evasive dives when a hunting bat approaches."),

    ("In industrial manufacturing, what capability allows ultrasonic drilling tools to carve non-circular holes in brittle materials like glass, quartz, and gemstones?",
     ["An ultrasonic horn vibrates an abrasive slurry against the brittle material at 20 kHz to 40 kHz, micro-chipping precise shapes",
      "Ultrasound heats the glass until it turns into gas",
      "Ultrasound fires laser beams through diamond nozzles",
      "Ultrasound acts as a high-pressure water jet"],
     "A", "OSC", "medium",
     "In ultrasonic machining (USM), a tool oscillating at ultrasonic frequencies drives micro-abrasive particles against hard, brittle workpieces, eroding complex non-round geometries without thermal stress.")
]

practice_data = [
    # 21-30: Properties & Infrasound / Ultrasound Comparisons
    ("A sound wave has a frequency of 15 Hz. Which category does this sound wave belong to?",
     ["Infrasonic sound", "Audible sound", "Ultrasonic sound", "Supersonic sound"],
     "A", "OSC", "easy",
     "Because 15 Hz is less than the lower human audible threshold of 20 Hz, it is classified as infrasound."),

    ("A sound wave has a frequency of 50,000 Hz (50 kHz). Which category does it belong to?",
     ["Ultrasonic sound", "Infrasonic sound", "Audible sound", "Subsonic sound"],
     "A", "OSC", "easy",
     "Because 50 kHz exceeds 20 kHz, it belongs to the ultrasonic frequency spectrum."),

    ("Which frequency among the following can be heard as a distinct audible sound by an average adult human?",
     ["5,000 Hz (5 kHz)", "10 Hz", "25,000 Hz", "50,000 Hz"],
     "A", "OSC", "easy",
     "5,000 Hz lies comfortably inside the 20 Hz to 20,000 Hz human hearing range. 10 Hz is infrasound, and 25 kHz / 50 kHz are ultrasound."),

    ("What is the wavelength in air (speed = 340 m/s) of the lowest audible sound wave frequency (20 Hz) for a human ear?",
     ["17 m", "0.017 m", "68 m", "1.7 m"],
     "A", "OSC", "medium",
     "\\lambda = v / \\nu = 340 / 20 = 17 m. The lowest audible sounds have long wavelengths up to 17 meters."),

    ("What is the wavelength in air (speed = 340 m/s) of the highest audible frequency (20,000 Hz) for a human ear?",
     ["0.017 m (1.7 cm)", "1.7 m", "17 m", "0.0017 m"],
     "A", "OSC", "medium",
     "\\lambda = v / \\nu = 340 / 20000 = 0.017 m = 1.7 cm. The highest audible sound has a compact wavelength of just 1.7 cm."),

    ("State whether the following statement is True or False: Elephants can communicate with herd members up to several kilometers away through low-frequency infrasonic vibrations in the ground.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Elephants produce deep rumbles around 15 Hz that travel through the soil and air across distances up to 5-10 km, detected by sensitive nerve corpuscles in their feet."),

    ("State whether the following statement is True or False: Ultrasonic waves have shorter wavelengths than audible sound waves in the same medium.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Because \\lambda = v / \\nu, higher frequencies (> 20 kHz) yield significantly shorter wavelengths, enabling sharp spatial resolution in imaging and flaw detection."),

    ("State whether the following statement is True or False: Dogs can hear sounds produced by a Galton whistle because their upper hearing limit is around 45 kHz.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Canines easily detect frequencies up to ~45-50 kHz, making silent whistles inaudible to humans but loud and clear to dogs."),

    ("State whether the following statement is True or False: Infrasound is sound moving faster than the speed of light.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Infrasound is simply sound with frequency below 20 Hz; it travels at the standard speed of sound in the given medium."),

    ("Why can ultrasound penetrate deep into metal blocks and human tissues with minimal scattering compared to audible sound?",
     ["Because its extremely short wavelength allows it to travel in tight, straight beam paths with very low diffraction around edges",
      "Because ultrasound particles are smaller than air molecules",
      "Because ultrasound waves have infinite velocity",
      "Because ultrasound produces intense magnetic fields"],
     "A", "OSC", "medium",
     "Higher frequencies correspond to very small wavelengths (millimeter to sub-millimeter scale), minimizing wave diffraction and allowing ultrasound to be directed in focused pencil-like beams.")
]

# Additional 20 questions to exam_data (total 40)
extra_exam = [
    ("What happens to the upper frequency hearing limit of human beings as they grow older (presbycusis)?",
     ["It declines progressively from 20 kHz down to 12 kHz to 14 kHz",
      "It increases up to 100 kHz",
      "It remains exactly identical throughout life",
      "It drops to zero at age 30"],
     "A", "OSC", "easy",
     "Aging leads to gradual degeneration of delicate high-frequency sensory hair cells near the base of the cochlea, lowering the audible threshold to ~12-14 kHz in older adults."),

    ("Which property of ultrasound allows it to be focused sharply into a narrow, directed acoustic beam?",
     ["Its short wavelength (\\lambda = v / \\nu)",
      "Its high electrical charge",
      "Its low speed in water",
      "Its transverse polarization"],
     "A", "OSC", "easy",
     "Because ultrasound has very high frequency, its wavelength is very small (often under a millimeter), minimizing beam divergence and diffraction spreading."),

    ("In industrial flaw detection, what happens to the ultrasound pulse when it encounters a crack in a metal block?",
     ["Part of the ultrasound wave is reflected early at the metal-air crack boundary back to the receiving probe",
      "The entire wave is completely destroyed",
      "The wave changes into an electric spark",
      "The frequency of the wave drops to 1 Hz"],
     "A", "OSC", "easy",
     "Because air inside a crack has vastly different acoustic impedance than solid metal, ultrasound strongly reflects at the defect boundary, producing a tell-tale flaw echo."),

    ("Which medical device uses the Doppler shift of reflected ultrasound waves to measure the speed and direction of blood flowing through heart valves and arteries?",
     ["Doppler ultrasound (color Doppler)",
      "Standard electrocardiogram (ECG)",
      "Stethoscope",
      "Digital sphygmomanometer"],
     "A", "OSC", "medium",
     "When ultrasound reflects off moving red blood cells, its frequency shifts proportionally to blood velocity (Doppler effect), allowing doctors to map arterial stenosis and heart valve leaks."),

    ("Why do rhinos and elephants exhibit anxious behavior hours before a tsunami or major earthquake strikes?",
     ["They sense low-frequency seismic infrasound vibrations traveling rapidly through the ground",
      "They have telepathic communication with ocean tides",
      "They can smell tectonic plates moving",
      "They see changes in cosmic rays"],
     "A", "OSC", "easy",
     "Infrasonic waves travel faster than surface tsunami waves and main shock tremors, alerting sensitive animals to impending cataclysms."),

    ("Assertion (A): Ultrasonic waves are used to clean spiraled tubing and delicate electronic watch mechanisms.\nReason (R): Ultrasonic cavitation produces intense localized scrubbing action that dislodges grime from hard-to-reach surfaces without damage.",
     ["Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A)",
      "Both Assertion (A) and Reason (R) are true, but Reason (R) is not the correct explanation",
      "Assertion (A) is true, but Reason (R) is false",
      "Assertion (A) is false, but Reason (R) is true"],
     "A", "OAR", "easy",
     "Cavitation micro-bubbles implode on complex surfaces, stripping grease and dirt from microscopic crevices."),

    ("State whether the following statement is True or False: Bats are completely blind and rely 100% solely on ultrasound to survive.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Bats are not blind; they have functional eyes but supplement or dominate night hunting using ultrasonic echolocation."),

    ("State whether the following statement is True or False: Ultrasound can be used to homogenize milk and kill pathogenic bacteria.",
     ["True", "False"],
     "A", "OTF", "easy",
     "High-power acoustic cavitation shears fat globules and disrupts bacterial cell walls, aiding pasteurization and homogenization."),

    ("A medical ultrasound scanner uses sound of frequency 4 MHz in soft tissue where sound speed is 1540 m/s. What is the wavelength of the ultrasound?",
     ["0.385 mm (0.000385 m)", "3.85 mm", "38.5 mm", "0.0385 mm"],
     "A", "OSC", "medium",
     "\\lambda = v / \\nu = 1540 / (4 * 10^6) = 0.000385 m = 0.385 mm (sub-millimeter resolution for fine anatomical structures)."),

    ("Why is a water-soluble acoustic gel applied to a patient's skin before performing an ultrasound scan?",
     ["To eliminate the air gap between the transducer and skin, ensuring efficient acoustic transmission without total reflection",
      "To disinfect the patient's skin against bacteria",
      "To numb the patient's skin with anesthetic",
      "To make the skin transparent to visible light"],
     "A", "OSC", "medium",
     "Acoustic impedance of air is vastly different from human tissue. Any tiny air pocket reflects 99.9% of ultrasound. Coupling gel matches acoustic impedance, channeling sound cleanly into the body.")
,
    ("What is the primary sensory mechanism that enables oceanic dolphins to locate schools of fish in muddy estuarine waters?",
     ["Ultrasonic echolocation using acoustic melon focusing",
      "Infrared heat sensing",
      "Electro-magnetic reception like sharks",
      "Visual optical magnification"],
     "A", "OSC", "easy",
     "Dolphins focus ultrasonic clicks through their fatty forehead melon organ. Reflections from fish swim bladders reveal prey location, size, and movement direction in zero visibility."),

    ("Which property of ultrasound enables it to blend immiscible liquids into permanent fine emulsions without chemical emulsifiers?",
     ["Intense acoustic cavitation shear stresses",
      "Chemical reduction by sonic electrons",
      "High temperature boiling",
      "Nuclear acoustic resonance"],
     "A", "OSC", "medium",
     "Cavitation micro-jets generate extreme localized hydrodynamic shear forces that break oil and water droplets down to nanoscale diameters, producing stable emulsions."),

    ("Why can seismic infrasound be detected thousands of kilometers away from an earthquake epicenter by sensitive barometers?",
     ["Infrasound waves undergo very low atmospheric and crustal attenuation due to their long wavelengths",
      "Infrasound travels through the core of the Earth at light speed",
      "Infrasound is amplified by the ionosphere",
      "Infrasound waves carry electric current"],
     "A", "OSC", "easy",
     "Low acoustic frequencies suffer minimal absorption, allowing microbarometers in international monitoring stations to detect atmospheric acoustic waves from distant earthquakes."),

    ("What is the relationship between the wavelength of a 2 MHz ultrasound wave in soft human tissue (v = 1540 m/s) and a 20 kHz audible sound wave in air (v = 340 m/s)?",
     ["The 2 MHz ultrasound wavelength is roughly 22 times shorter (0.77 mm vs 17 mm)",
      "Both wavelengths are identical",
      "The ultrasound wave has a 10 times longer wavelength",
      "The ultrasound wavelength is 1 meter long"],
     "A", "OSC", "medium",
     "In tissue, \lambda_{US} = 1540 / (2 * 10^6) = 0.00077 m = 0.77 mm. In air, \lambda_{audible} = 340 / 20000 = 0.017 m = 17 mm. The ultrasound wavelength is 0.77 / 17 \approx 1/22 of the audible wavelength."),

    ("State whether the following statement is True or False: Certain moths can detect the ultrasonic clicks of insectivorous bats and perform sudden evasive maneuvers.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Tiger moths and other night-flying insects have ultrasonic hearing organs tuned to bat frequencies (20-100 kHz), initiating spiral dives to escape predation."),

    ("State whether the following statement is True or False: Medical ultrasound imaging can produce clear anatomical images of internal bone marrow through thick adult skull bones.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Dense bone strongly absorbs and reflects ultrasound, creating acoustic shadows that prevent diagnostic scanning of deep bone interiors without specialized transcranial windows."),

    ("Which of the following medical procedures is performed using high-energy focused ultrasound?",
     ["Shattering kidney stones and ablating prostate tumors",
      "Measuring lung oxygen saturation",
      "Treating viral infections with antibiotics",
      "Taking chest X-rays"],
     "A", "OSC", "easy",
     "High-Intensity Focused Ultrasound (HIFU) and lithotripsy focus destructive acoustic energy non-invasively onto target tissues like stones or tumors."),

    ("What type of wave is ultrasound when propagating through soft body tissue?",
     ["Mechanical longitudinal wave of alternating compressions and rarefactions",
      "Transverse electromagnetic wave",
      "Polarized shear wave only",
      "Gravitational wave"],
     "A", "OSC", "easy",
     "In soft tissues and bodily fluids, ultrasound travels exclusively as longitudinal pressure waves."),

    ("Why are pregnant women routinely advised to undergo diagnostic ultrasound scans rather than abdominal X-rays?",
     ["Ultrasound uses non-ionizing mechanical vibrations that do not damage fetal chromosomes",
      "Ultrasound is cheaper than paper",
      "X-rays cannot penetrate skin",
      "Ultrasound cures genetic disorders"],
     "A", "OSC", "easy",
     "Ultrasound is non-ionizing radiation and poses zero risk of radiation-induced DNA mutations to the developing embryo."),

    ("How does a Galton whistle generate ultrasonic acoustic frequencies above 20 kHz?",
     ["A narrow high-velocity air jet strikes a small resonant pipe cavity whose acoustic resonant frequency exceeds 20 kHz",
      "An electric spark creates radio noise",
      "A quartz laser generates light pulses",
      "A chemical reaction releases helium"],
     "A", "OSC", "medium",
     "The small physical length of the pipe cavity ensures a very short fundamental wavelength, producing high-frequency acoustic resonance above the human audible limit.")
]

# Additional 20 questions to practice_data (total 30)
extra_practice = [
    ("Which of the following creatures emits sounds with frequency lower than 20 Hz?",
     ["Blue whale", "Bat", "Dolphin", "Dog"],
     "A", "OSC", "easy",
     "Blue whales communicate using deep infrasound tones around 10-20 Hz that propagate across ocean basins."),

    ("What is the frequency of a sound wave whose time period is 0.00002 seconds (20 microseconds)?",
     ["50,000 Hz (50 kHz, Ultrasonic)",
      "20,000 Hz",
      "5,000 Hz",
      "500 Hz"],
     "A", "OSC", "easy",
     "\\nu = 1 / T = 1 / 0.00002 = 50,000 Hz = 50 kHz. This is in the ultrasonic spectrum."),

    ("Why do seismologists deploy sensitive infrasound sensor networks around active volcanoes?",
     ["Magma movements and gas venting inside volcanic vents emit low-frequency infrasound before explosive eruptions",
      "Infrasound stops volcanic lava from erupting",
      "Volcanoes only emit ultrasound",
      "Infrasound turns magma into basalt rock"],
     "A", "OSC", "easy",
     "Infrasound travels through the atmosphere with very low attenuation, providing early warning of sub-surface volcanic pressure build-up."),

    ("State whether the following statement is True or False: Ultrasonic waves can be deflected by standard glass lenses and mirrors obeying optical reflection laws.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Like all waves, ultrasound obeys reflection and refraction laws, and acoustic lenses are used to focus beam pulses."),

    ("State whether the following statement is True or False: A sound of frequency 18 Hz is audible to healthy human teenagers.",
     ["False", "True"],
     "A", "OTF", "easy",
     "18 Hz lies below the minimum human audible threshold of 20 Hz (it is infrasound)."),

    ("What is the frequency range of ultrasound used in standard prenatal fetal diagnostic sonography?",
     ["2 MHz to 7 MHz (2,000,000 Hz to 7,000,000 Hz)",
      "20 Hz to 20,000 Hz",
      "100 Hz to 1,000 Hz",
      "100 MHz to 1 GHz"],
     "A", "OSC", "medium",
     "Diagnostic abdominal fetal ultrasound operates between 2 MHz and 7 MHz, providing a good compromise between depth penetration and sub-millimeter image resolution."),

    ("An ultrasonic flaw detector emits a pulse of 2.5 MHz into an aluminum block where sound speed is 6000 m/s. What is the wavelength of the pulse?",
     ["2.4 mm (0.0024 m)", "24 mm", "0.24 mm", "240 mm"],
     "A", "OSC", "medium",
     "\\lambda = v / \\nu = 6000 / (2.5 * 10^6) = 0.0024 m = 2.4 mm."),

    ("What property of ultrasound enables it to destroy kidney stones without causing skin cuts?",
     ["Energy concentration at the geometric focal zone of acoustic transducers",
      "Ultrasound dissolves the stone with acidic chemicals",
      "Ultrasound freezes the skin",
      "Ultrasound converts calcium into water"],
     "A", "OSC", "easy",
     "Acoustic shockwaves pass harmlessly through dispersed skin areas but converge onto a tiny focal volume where immense compressive stress fractures the stone."),

    ("Which of the following devices does NOT rely on ultrasound?",
     ["Optical laser barcode scanner",
      "Echocardiogram machine",
      "SONAR depth sounder",
      "Ultrasonic jewelry cleaner"],
     "A", "OSC", "easy",
     "Barcode scanners use electromagnetic laser light, not acoustic ultrasound."),

    ("Why do tigers emit deep roars containing low-frequency infrasound components below 18 Hz?",
     ["Infrasound penetrates thick jungle foliage across kilometers and can induce temporary sensory paralysis in prey animals",
      "To attract butterflies",
      "To scare away thunderclouds",
      "Because tigers cannot produce high pitches"],
     "A", "OSC", "medium",
     "Tiger roars contain low-frequency infrasound (around 18 Hz) that travels long distances through dense forests and creates an involuntary physical freeze reaction in prey nervous systems.")
,
    ("What is the frequency of a sound wave whose wavelength in air (v = 340 m/s) is 3.4 cm (0.034 m)?",
     ["10,000 Hz (10 kHz, Audible)", "1,000 Hz", "34,000 Hz", "500 Hz"],
     "A", "OSC", "easy",
     "\nu = v / \lambda = 340 / 0.034 = 10,000 Hz = 10 kHz (audible sound)."),

    ("What is the frequency of a sound wave whose wavelength in water (v = 1500 m/s) is 3.0 cm (0.03 m)?",
     ["50,000 Hz (50 kHz, Ultrasonic)", "15,000 Hz", "5,000 Hz", "500 Hz"],
     "A", "OSC", "easy",
     "\nu = v / \lambda = 1500 / 0.03 = 50,000 Hz = 50 kHz (ultrasound)."),

    ("Which creature is famous for producing deep 5 Hz infrasound calls that can be detected through the savanna ground across several kilometers?",
     ["Rhinoceros", "Cheetah", "Giraffe", "Baboon"],
     "A", "OSC", "easy",
     "Rhinoceroses emit low-frequency infrasound down to 5 Hz for territory and group coordination."),

    ("State whether the following statement is True or False: Dogs can hear frequencies up to 50,000 Hz, while cats can hear frequencies up to 64,000 Hz.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Both domestic canines and felines have evolved broad ultrasonic auditory bandwidths to detect small prey."),

    ("State whether the following statement is True or False: Infrasound waves travel slower than audible sound waves in the exact same air sample.",
     ["False", "True"],
     "A", "OTF", "easy",
     "All acoustic waves travel at the identical speed of sound in a given medium regardless of frequency (v is constant)."),

    ("In non-destructive testing, what causes a flaw echo to appear between the initial pulse and the back-wall echo on the display screen?",
     ["A crack located halfway through the thickness of the metal reflects part of the pulse early",
      "The metal block is magnetized",
      "The transducer battery is failing",
      "Sound speed accelerates inside the flaw"],
     "A", "OSC", "easy",
     "The flaw's internal boundary reflects the wave before it reaches the far boundary of the block, displaying an intermediate peak."),

    ("What frequency range is generally utilized in industrial ultrasonic plastic welding?",
     ["15 kHz to 40 kHz", "1 Hz to 10 Hz", "1 GHz to 5 GHz", "100 MHz to 200 MHz"],
     "A", "OSC", "medium",
     "Ultrasonic plastic welders operate between 15 kHz and 40 kHz, converting mechanical vibrations into frictional heat at the joint interface."),

    ("Why can elephants detect seismic tremors through their feet before hearing airborne sounds?",
     ["Raleigh and Love seismic ground waves travel directly into the foot pads where specialized Pacinian corpuscles detect low-frequency vibrations",
      "Elephants put their ears on the ground",
      "Elephant skin has magnetic receptors",
      "Elephant tusks act as radio antennas"],
     "A", "OSC", "easy",
     "Pacinian corpuscles in elephant feet are sensitive mechanoreceptors that register deep ground-borne infrasonic waves."),

    ("Which property of ultrasonic waves allows them to break up bacterial biofilms and clean dental tartar in ultrasonic scalers?",
     ["High-frequency micro-vibration and localized cavitation implosions",
      "Chemical release of chlorine bleach",
      "Thermal laser burning of gums",
      "Freezing water into ice micro-needles"],
     "A", "OSC", "easy",
     "Ultrasonic dental scalers vibrate at 25-35 kHz with water coolant, micro-chipping tartar and generating cavitation that disrupts bacterial plaque."),

    ("What is the ratio of human upper hearing limit (20 kHz) to elephant lower communication frequency (~10 Hz)?",
     ["2,000 : 1", "100 : 1", "20 : 1", "10,000 : 1"],
     "A", "OSC", "easy",
     "20,000 Hz / 10 Hz = 2000.")
]

mock_data = [
    # 71: Three Acoustic Frequency Zones Master Diagram
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <text x="35" y="25" fill="#facc15" font-size="11" font-weight="bold">The Three Acoustic Frequency Spectrum Zones</text>
  <!-- Zone 1: Infrasound -->
  <rect x="25" y="45" width="85" height="70" fill="#f87171" fill-opacity="0.2" stroke="#f87171" stroke-width="2" rx="4"/>
  <text x="32" y="65" fill="#f87171" font-size="10" font-weight="bold">INFRASOUND</text>
  <text x="35" y="85" fill="#cbd5e1" font-size="9">&lt; 20 Hz</text>
  <text x="30" y="105" fill="#cbd5e1" font-size="8">Earthquakes, Rhinos</text>
  <!-- Zone 2: Audible -->
  <rect x="115" y="45" width="110" height="70" fill="#4ade80" fill-opacity="0.2" stroke="#4ade80" stroke-width="2" rx="4"/>
  <text x="125" y="65" fill="#4ade80" font-size="10" font-weight="bold">AUDIBLE SOUND</text>
  <text x="125" y="85" fill="#cbd5e1" font-size="9">20 Hz – 20,000 Hz</text>
  <text x="130" y="105" fill="#cbd5e1" font-size="8">Normal Human Ear</text>
  <!-- Zone 3: Ultrasound -->
  <rect x="230" y="45" width="85" height="70" fill="#38bdf8" fill-opacity="0.2" stroke="#38bdf8" stroke-width="2" rx="4"/>
  <text x="237" y="65" fill="#38bdf8" font-size="10" font-weight="bold">ULTRASOUND</text>
  <text x="240" y="85" fill="#cbd5e1" font-size="9">&gt; 20,000 Hz</text>
  <text x="235" y="105" fill="#cbd5e1" font-size="8">Bats, Sonography</text>
  <!-- Frequency axis arrow -->
  <line x1="25" y1="140" x2="315" y2="140" stroke="#facc15" stroke-width="2"/>
  <polygon points="310,137 318,140 310,143" fill="#facc15"/>
  <text x="120" y="155" fill="#facc15" font-size="10">Frequency Scale (Hz)</text>
  <text x="50" y="180" fill="#cbd5e1" font-size="9.5">Humans hear strictly between 20 Hz and 20 kHz</text>
</svg>
</div>
According to the master frequency spectrum chart shown above, what are the exact frequency boundaries that define the audible hearing range of a normal human ear?""",
     ["Between 20 Hz and 20,000 Hz (20 kHz)""",
     "Below 20 Hz only""",
     "Above 20,000 Hz only""",
     "Between 0 Hz and 100 Hz"],
     "A", "OSC", "easy""",
     "Human hearing is biologically bounded between 20 Hz (lower limit, below which is infrasound) and 20,000 Hz (upper limit, above which is ultrasound)."),

    # 72: Bat Echolocation Vector Diagram
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Bat shape -->
  <path d="M 50,85 Q 65,60 80,85 Q 95,60 110,85 Q 80,105 50,85 Z" fill="#94a3b8"/>
  <text x="60" y="115" fill="#cbd5e1" font-size="9" font-weight="bold">Bat</text>
  <!-- Moth insect -->
  <circle cx="280" cy="85" r="8" fill="#facc15"/>
  <line x1="272" y1="77" x2="260" y2="65" stroke="#facc15" stroke-width="2"/>
  <line x1="288" y1="77" x2="300" y2="65" stroke="#facc15" stroke-width="2"/>
  <text x="265" y="115" fill="#facc15" font-size="9" font-weight="bold">Insect Prey</text>
  <!-- Emitted waves (Blue) -->
  <path d="M 120,70 A 40,40 0 0,1 120,100" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
  <path d="M 140,60 A 60,60 0 0,1 140,110" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
  <path d="M 160,50 A 80,80 0 0,1 160,120" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
  <text x="130" y="40" fill="#38bdf8" font-size="9">Emitted Ultrasound (&gt; 50 kHz)</text>
  <!-- Reflected echo waves (Red dashed) -->
  <path d="M 240,65 A 50,50 0 0,0 240,105" fill="none" stroke="#f43f5e" stroke-width="2" stroke-dasharray="4,3"/>
  <path d="M 210,55 A 70,70 0 0,0 210,115" fill="none" stroke="#f43f5e" stroke-width="2" stroke-dasharray="4,3"/>
  <text x="180" y="150" fill="#f43f5e" font-size="9">Reflected Echo Pulses</text>
  <text x="50" y="180" fill="#cbd5e1" font-size="10">Echolocation: Bat calculates prey distance from echo delay: d = v·t / 2</text>
</svg>
</div>
How does a bat calculate the precise location and distance of a flying moth in total darkness, as illustrated in the echolocation diagram?""",
     ["By emitting high-frequency ultrasonic clicks and measuring the time delay and direction of the reflected echo pulses (d = v*t / 2)""",
     "By smelling the moth's pheromones across the air""",
     "By using infrared night-vision eyesight""",
     "By feeling magnetic field changes with its wings"],
     "A", "OSC", "easy""",
     "The bat emits ultrasound bursts (> 50 kHz). The pulses bounce off the moth and return as an echo. The bat's brain processes the round-trip time t and ear binaural difference to pinpoint the insect's distance and flight speed."),

    # 73: Ultrasonic Metal Flaw Detection
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Steel Block -->
  <rect x="40" y="40" width="260" height="110" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
  <text x="50" y="60" fill="#cbd5e1" font-size="10">Solid Steel Block</text>
  <!-- Probe on left -->
  <rect x="25" y="70" width="15" height="30" fill="#38bdf8"/>
  <text x="10" y="65" fill="#38bdf8" font-size="8">Transmitter</text>
  <!-- Crack / defect -->
  <ellipse cx="160" cy="85" rx="4" ry="18" fill="#f43f5e"/>
  <text x="150" y="60" fill="#f43f5e" font-size="9" font-weight="bold">Internal Defect</text>
  <!-- Normal detector on right -->
  <rect x="300" y="110" width="15" height="25" fill="#4ade80"/>
  <text x="270" y="145" fill="#4ade80" font-size="8">Detector 2</text>
  <!-- Blocked wave on top half -->
  <line x1="40" y1="85" x2="155" y2="85" stroke="#38bdf8" stroke-width="2.5"/>
  <line x1="155" y1="85" x2="40" y2="95" stroke="#f87171" stroke-width="2" stroke-dasharray="3,3"/>
  <text x="50" y="105" fill="#f87171" font-size="8.5">Reflected Flaw Echo</text>
  <!-- Passed wave on bottom half -->
  <line x1="40" y1="125" x2="300" y2="125" stroke="#4ade80" stroke-width="2"/>
  <text x="50" y="175" fill="#cbd5e1" font-size="10">Flaw detection: Internal void reflects ultrasound early before back wall</text>
</svg>
</div>
In the non-destructive metal flaw testing setup shown above, how does the technician identify the presence of an internal defect inside the metal block?""",
     ["The defect causes an early reflected echo to return to the transmitter before the wave reaches the rear wall""",
     "The defect makes the metal block melt at the surface""",
     "The defect absorbs 100% of the block's magnetic field""",
     "The defect changes the color of the steel to red"],
     "A", "OSC", "easy""",
     "Ultrasound travels through clean solid metal. When it hits the metal-air boundary of a hidden internal crack, part of the wave reflects back prematurely, producing a distinctive intermediate pulse on the oscilloscope screen."),

    # 74: Ultrasonic Cleaning Bath Cavitation
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Tank with cleaning liquid -->
  <rect x="50" y="45" width="240" height="100" fill="#0284c7" fill-opacity="0.2" stroke="#38bdf8" stroke-width="2"/>
  <!-- Dirty gear component submerged -->
  <circle cx="170" cy="95" r="25" fill="#475569" stroke="#94a3b8" stroke-width="3"/>
  <circle cx="170" cy="95" r="10" fill="#0f172a"/>
  <!-- Ultrasonic Transducer below -->
  <rect x="110" y="150" width="120" height="15" fill="#facc15" rx="3"/>
  <text x="120" y="162" fill="#0f172a" font-size="9" font-weight="bold">Ultrasonic Transducer (40 kHz)</text>
  <!-- Microscopic Cavitation Bubbles -->
  <g fill="#e2e8f0">
    <circle cx="130" cy="80" r="3"/><circle cx="140" cy="90" r="2"/><circle cx="150" cy="75" r="3.5"/>
    <circle cx="190" cy="80" r="2"/><circle cx="205" cy="95" r="3"/><circle cx="195" cy="110" r="2.5"/>
  </g>
  <text x="60" y="35" fill="#38bdf8" font-size="10" font-weight="bold">Acoustic Cavitation Implosions Strip Grease</text>
  <text x="50" y="180" fill="#cbd5e1" font-size="9.5">Imploding micro-bubbles clean intricate spiral jewelry and electronics</text>
</svg>
</div>
What physical mechanism allows an ultrasonic cleaning tank to remove dirt and grease from intricately shaped watch parts and electronic components?""",
     ["Acoustic cavitation: Rapid pressure cycles create microscopic vapor bubbles that implode violently against surfaces, scrubbing off grime""",
     "Chemical corrosion of the dirty parts""",
     "Electrolytic acid etching""",
     "High-temperature vapor boiling"],
     "A", "OSC", "easy""",
     "Ultrasound creates alternating high and low pressure cycles that produce micro-bubbles (cavitation). These collapse with intense localized shockwaves and micro-jets that scrub away dirt without scratching delicate mechanisms."),

    # 75: Medical Ultrasonography (Sonography) Probe
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Transducer Probe -->
  <rect x="140" y="25" width="60" height="30" fill="#475569" rx="4"/>
  <rect x="145" y="55" width="50" height="6" fill="#38bdf8"/>
  <text x="148" y="45" fill="#f8fafc" font-size="9">US Probe</text>
  <!-- Coupling gel layer -->
  <line x1="110" y1="65" x2="230" y2="65" stroke="#38bdf8" stroke-width="3"/>
  <text x="240" y="68" fill="#38bdf8" font-size="8">Acoustic Gel</text>
  <!-- Human Abdomen Tissue -->
  <rect x="40" y="68" width="260" height="85" fill="#991b1b" fill-opacity="0.2" stroke="#f87171" stroke-width="1.5"/>
  <!-- Internal organ (e.g. Kidney/Liver) -->
  <ellipse cx="170" cy="115" rx="40" ry="22" fill="#7f1d1d" stroke="#fca5a5" stroke-width="2"/>
  <text x="150" y="118" fill="#fca5a5" font-size="9.5">Internal Organ</text>
  <!-- Sound beam spreading down -->
  <path d="M 145,65 L 100,145 L 240,145 L 195,65 Z" fill="#38bdf8" fill-opacity="0.08"/>
  <text x="60" y="175" fill="#cbd5e1" font-size="10">Sonography: Safe mechanical sound waves image soft internal organs</text>
</svg>
</div>
Why is water-based acoustic gel always spread between the ultrasound probe and the patient's skin during medical sonography?""",
     ["To eliminate trapped air pockets, ensuring acoustic impedance matching so sound penetrates smoothly into body tissues without reflecting away""",
     "To numb the patient's skin against electrical shocks""",
     "To lubricate the probe so it moves faster than sound""",
     "To heat up internal organs for thermal photography"],
     "A", "OSC", "medium""",
     "Because air and skin have vastly different acoustic impedances, even a microscopic air gap reflects over 99% of ultrasound. The coupling gel bridges the gap, allowing ultrasound pulses to enter the body."),

    # 76: Extracorporeal Shock Wave Lithotripsy (ESWL)
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Acoustic reflector focusing shockwaves -->
  <path d="M 50,30 A 100,100 0 0,0 50,160" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <text x="40" y="20" fill="#38bdf8" font-size="9">Ultrasound Emitter</text>
  <!-- Kidney Stone at focal point -->
  <circle cx="240" cy="95" r="9" fill="#facc15" stroke="#f59e0b" stroke-width="2"/>
  <text x="220" y="75" fill="#facc15" font-size="9" font-weight="bold">Kidney Stone</text>
  <!-- Converging sound beams to stone -->
  <line x1="55" y1="45" x2="240" y2="95" stroke="#f43f5e" stroke-width="2"/>
  <line x1="50" y1="95" x2="240" y2="95" stroke="#f43f5e" stroke-width="2"/>
  <line x1="55" y1="145" x2="240" y2="95" stroke="#f43f5e" stroke-width="2"/>
  <text x="130" y="120" fill="#f43f5e" font-size="9">Focused Shockwaves</text>
  <text x="60" y="175" fill="#cbd5e1" font-size="10">Lithotripsy: Ultrasonic shockwaves pulverize kidney stones without incisions</text>
</svg>
</div>
In the lithotripsy procedure illustrated above, how do ultrasonic shockwaves safely break brittle kidney stones without damaging surrounding skin and muscle?""",
     ["Shockwaves enter harmlessly over a wide skin area and converge only at the precise internal focal point, concentrating shattering energy onto the stone""",
     "The patient drinks ultrasound liquid before treatment""",
     "Ultrasound laser beams burn the skin open""",
     "Ultrasound creates an electric magnetic field that dissolves the kidney"],
     "A", "OSC", "easy""",
     "Low-pressure sound waves spread across a wide body cross-section, causing no tissue trauma; parabolic reflection converges all acoustic energy precisely onto the stone, shattering it into fine fragments."),

    # 77: Galton's Silent Dog Whistle
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Whistle -->
  <rect x="40" y="75" width="80" height="25" rx="4" fill="#94a3b8"/>
  <circle cx="110" cy="87" r="6" fill="#475569"/>
  <text x="35" y="65" fill="#cbd5e1" font-size="9.5" font-weight="bold">Galton's Whistle (~30 kHz)</text>
  <!-- Human ear icon crossed out -->
  <circle cx="190" cy="65" r="14" fill="#f87171" fill-opacity="0.2" stroke="#f87171"/>
  <text x="180" y="70" fill="#f87171" font-size="12">👂</text>
  <line x1="175" y1="50" x2="205" y2="80" stroke="#f87171" stroke-width="2"/>
  <text x="160" y="95" fill="#f87171" font-size="8.5">Inaudible to Humans</text>
  <!-- Dog ear icon checked -->
  <circle cx="280" cy="65" r="14" fill="#4ade80" fill-opacity="0.2" stroke="#4ade80"/>
  <text x="270" y="70" fill="#4ade80" font-size="12">🐕</text>
  <text x="250" y="95" fill="#4ade80" font-size="8.5">Heard clearly by Dog</text>
  <text x="50" y="145" fill="#facc15" font-size="10">Dogs hear up to ~50 kHz; Humans cut off at 20 kHz</text>
  <text x="50" y="175" fill="#cbd5e1" font-size="9.5">Silent dog training whistle emits ultrasound around 30 kHz</text>
</svg>
</div>
Why is Galton's dog whistle called a 'silent whistle' even though it emits an intensely loud acoustic tone?""",
     ["It produces sound around 30 kHz, which is above the 20 kHz human hearing limit (silent to humans) but well within a dog's 50 kHz range""",
     "Because it emits no sound waves at all""",
     "Because the sound only travels through the ground""",
     "Because it uses radio waves instead of sound"],
     "A", "OSC", "easy""",
     "Human ears cannot register sound frequencies above 20 kHz. Dogs can perceive frequencies up to 50 kHz, so a 30 kHz whistle is completely silent to human bystanders while commanding the dog."),

    # 78: Infrasound Transmission across Continents
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <text x="35" y="25" fill="#f87171" font-size="11" font-weight="bold">Long-Distance Propagation of Infrasound (&lt; 20 Hz)</text>
  <!-- Low frequency long wavelength -->
  <path d="M 30,95 Q 75,40 120,95 T 210,95 T 300,95" fill="none" stroke="#f87171" stroke-width="3"/>
  <text x="40" y="130" fill="#f87171" font-size="10">Huge Wavelength (\\lambda &gt; 17 m)</text>
  <text x="40" y="150" fill="#4ade80" font-size="9.5">• Minimal atmospheric attenuation over thousands of km</text>
  <text x="40" y="170" fill="#cbd5e1" font-size="9.5">• Used to monitor nuclear explosions, volcanic eruptions &amp; avalanches</text>
</svg>
</div>
Why can infrasonic sound waves generated by volcanic eruptions or nuclear tests travel thousands of kilometers through the atmosphere without fading away?""",
     ["Because low-frequency waves with huge wavelengths suffer remarkably little atmospheric absorption and scattering compared to high-frequency sounds""",
     "Because infrasound travels at the speed of light""",
     "Because infrasound is carried by radio towers""",
     "Because infrasound creates its own vacuum channel"],
     "A", "OSC", "medium""",
     "Atmospheric acoustic attenuation increases with the square of frequency. Ultra-low infrasonic frequencies (< 20 Hz) experience minimal thermal and viscous absorption, circumnavigating the globe multiple times."),

    # 79: Comparison of Animal Hearing Ranges
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <text x="30" y="25" fill="#facc15" font-size="11" font-weight="bold">Animal Hearing Range Comparison (Hz)</text>
  <!-- Elephant -->
  <rect x="30" y="45" width="90" height="18" fill="#f87171" rx="3"/>
  <text x="130" y="58" fill="#f87171" font-size="9.5">Elephant: 14 Hz – 12,000 Hz (Infrasound)</text>
  <!-- Human -->
  <rect x="50" y="75" width="130" height="18" fill="#4ade80" rx="3"/>
  <text x="190" y="88" fill="#4ade80" font-size="9.5">Human: 20 Hz – 20,000 Hz</text>
  <!-- Dog -->
  <rect x="65" y="105" width="160" height="18" fill="#38bdf8" rx="3"/>
  <text x="235" y="118" fill="#38bdf8" font-size="9.5">Dog: ~50 Hz – 45,000 Hz</text>
  <!-- Bat -->
  <rect x="90" y="135" width="220" height="18" fill="#ec4899" rx="3"/>
  <text x="120" y="148" fill="#0f172a" font-size="9" font-weight="bold">Bat: 1,000 Hz – 120,000 Hz (Ultrasound)</text>
  <text x="50" y="178" fill="#cbd5e1" font-size="9">Different species evolved specialized auditory windows for survival</text>
</svg>
</div>
According to the auditory span comparison, which animal has the highest upper hearing frequency limit, reaching up to 120,000 Hz (120 kHz)?""",
     ["Bats", "Humans", "Elephants", "Horses"],
     "A", "OSC", "easy""",
     "Bats possess specialized auditory structures capable of hearing ultrasonic frequencies up to 100-120 kHz, enabling high-resolution echolocation."),

    # 80: Echocardiography Doppler Blood Flow
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <text x="35" y="25" fill="#38bdf8" font-size="11" font-weight="bold">Color Doppler Echocardiography</text>
  <!-- Blood vessel/Heart chamber -->
  <rect x="40" y="55" width="260" height="60" rx="10" fill="#1e293b" stroke="#64748b"/>
  <!-- Red blood cells moving right -->
  <circle cx="90" cy="85" r="7" fill="#f43f5e"/>
  <circle cx="150" cy="85" r="7" fill="#f43f5e"/>
  <circle cx="210" cy="85" r="7" fill="#f43f5e"/>
  <line x1="225" y1="85" x2="250" y2="85" stroke="#f43f5e" stroke-width="2"/>
  <polygon points="245,82 255,85 245,88" fill="#f43f5e"/>
  <text x="210" y="70" fill="#f43f5e" font-size="9">Flow Direction</text>
  <!-- Ultrasound beam at angle theta -->
  <line x1="100" y1="35" x2="150" y2="85" stroke="#38bdf8" stroke-width="2"/>
  <text x="50" y="145" fill="#facc15" font-size="10">Doppler frequency shift: \Deltaf = 2 · f₀ · (v / c) · cos \theta</text>
  <text x="50" y="175" fill="#cbd5e1" font-size="9.5">Measures real-time cardiac output and heart valve leakage</text>
</svg>
</div>
How does color Doppler echocardiography measure the speed of blood flowing through heart valves without inserting physical probes into the bloodstream?""",
     ["By detecting the frequency shift (Doppler shift) of ultrasound waves reflecting off moving red blood cells""",
     "By measuring the temperature rise of blood""",
     "By counting the red blood cells optically""",
     "By measuring magnetic resistance of hemoglobin"],
     "A", "OSC", "medium""",
     "When ultrasound hits moving red blood cells, the reflected wave frequency is shifted higher (moving toward probe) or lower (moving away). The Doppler formula converts this frequency shift directly into blood velocity and flow direction."),

    # 81: Sub-millimeter Resolution of Ultrasound
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <rect x="25" y="25" width="290" height="140" rx="8" fill="#1e293b" stroke="#facc15" stroke-width="2"/>
  <text x="45" y="55" fill="#facc15" font-size="11" font-weight="bold">Acoustic Resolution Invariant:</text>
  <text x="45" y="85" fill="#e2e8f0" font-size="11">Minimum resolvable flaw size \approx Wavelength (\\lambda)</text>
  <text x="45" y="115" fill="#38bdf8" font-size="10.5">Audible Sound (1 kHz in steel): \\lambda = 5000 / 1000 = 5.0 m</text>
  <text x="45" y="145" fill="#4ade80" font-size="10.5">Ultrasound (5 MHz in steel): \\lambda = 5000 / (5·10⁶) = 1.0 mm</text>
</svg>
</div>
Why can high-frequency ultrasound detect tiny 1 mm hairline cracks in metal blocks while audible sound waves cannot?""",
     ["Because wave diffraction prevents detection of defects smaller than the wavelength; 5 MHz ultrasound has a tiny 1 mm wavelength, resolving minute cracks""",
     "Because audible sound cannot enter metal at all""",
     "Because ultrasound creates its own x-ray illumination""",
     "Because audible sound waves travel faster than 5 MHz waves"],
     "A", "OSC", "medium""",
     "An acoustic wave simply diffracts around obstacles smaller than its wavelength. Audible sound in steel has wavelengths of several meters, ignoring tiny cracks. 5 MHz ultrasound has a 1 mm wavelength, reflecting strongly off millimeter flaws."),

    # 82: Master Chapter 12 Topic 2 Classification Summary
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <rect x="20" y="20" width="300" height="150" rx="8" fill="#1e293b" stroke="#4ade80" stroke-width="2"/>
  <text x="40" y="45" fill="#facc15" font-size="11" font-weight="bold">Chapter 12 Topic 2 Summary:</text>
  <text x="40" y="70" fill="#f87171" font-size="10">• Infrasound: &lt; 20 Hz (Rhinos, Earthquakes, Volcanoes)</text>
  <text x="40" y="95" fill="#4ade80" font-size="10">• Audible: 20 Hz – 20,000 Hz (Normal human hearing)</text>
  <text x="40" y="120" fill="#38bdf8" font-size="10">• Ultrasound: &gt; 20,000 Hz (Bats, Dolphins, Sonography)</text>
  <text x="40" y="145" fill="#ec4899" font-size="10">• Applications: NDT Flaw Detection, Lithotripsy, Cavitation</text>
</svg>
</div>
Which frequency range is correctly paired with its defining characteristic according to the Chapter 12 syllabus?""",
     ["Ultrasound: Frequencies above 20 kHz, used for non-destructive testing and medical sonography""",
     "Infrasound: Frequencies above 20 kHz, used by bats""",
     "Audible sound: Frequencies below 20 Hz, heard by elephants""",
     "Ultrasound: Sound that travels in a vacuum"],
     "A", "OSC", "easy""",
     "Ultrasound spans frequencies above 20 kHz and powers non-destructive testing, sonar, cleaning baths, and medical sonography.")
]

def generate():
    all_qs = []
    
    # 40 Exam (20 from exam_data + 20 from extra_exam)
    full_exam = exam_data + extra_exam
    for i, item in enumerate(full_exam, start=1):
        qcode = f"{TOPIC_CODE}-{item[3]}-{i:03d}"
        opts = [{"text": o, "isCorrect": (chr(65+idx) == item[2])} for idx, o in enumerate(item[1])] if item[3] != "OTF" else [
            {"text": "True", "isCorrect": (item[2] == "A")},
            {"text": "False", "isCorrect": (item[2] == "B")}
        ]
        all_qs.append(make_q(qcode, TOPIC_CODE, item[0], opts, item[2], item[3], item[4], "exam", "standard", item[5]))

    # 30 Practice (10 from practice_data + 20 from extra_practice)
    full_practice = practice_data + extra_practice
    for i, item in enumerate(full_practice, start=41):
        qcode = f"{TOPIC_CODE}-{item[3]}-{i:03d}"
        opts = [{"text": o, "isCorrect": (chr(65+idx) == item[2])} for idx, o in enumerate(item[1])] if item[3] != "OTF" else [
            {"text": "True", "isCorrect": (item[2] == "A")},
            {"text": "False", "isCorrect": (item[2] == "B")}
        ]
        all_qs.append(make_q(qcode, TOPIC_CODE, item[0], opts, item[2], item[3], item[4], "practice", "standard", item[5]))

    # 12 Mock
    for i, item in enumerate(mock_data, start=71):
        qcode = f"{TOPIC_CODE}-OSC-{i:03d}"
        opts = [{"text": o, "isCorrect": (chr(65+idx) == item[2])} for idx, o in enumerate(item[1])]
        all_qs.append(make_q(qcode, TOPIC_CODE, item[0], opts, item[2], item[3], item[4], "mock", "foundation", item[5]))

    out_file = "scripts/ch12_topic2.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)
    print(f"Generated {len(all_qs)} questions for {TOPIC_CODE} -> {out_file}")

if __name__ == "__main__":
    generate()
